from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import PolicyholderForm, InsuranceForm, PolicyholdersSearchForm
from .models import Policyholder, Insurance
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .mixin import InsuranceOwnOrStaffMixin, UserInsuranceQuerySetMixin, StaffRequiredMixin, InsuranceSuccessUrlMixin, \
    CurrentPolicyholderMixin

from django.db.models import Sum
from django.contrib import messages
# Create your views here.


"""domovska stránka"""
class HomeView(TemplateView):
    template_name = 'policyholders/homepage.html'


"""---------------CRUD pre Poistenca - ľudí-----------------"""
class PolicyholderListView(LoginRequiredMixin,StaffRequiredMixin,ListView):
    model = Policyholder
    template_name = "policyholders/policyholder_list.html" #cesta k šablone
    context_object_name = "policyholders"  #ako to budeme volať v šablone(templates)
    paginate_by = 10

    def get_queryset(self):
        queryset = Policyholder.objects.all()

        first_name = self.request.GET.get("first_name")
        last_name = self.request.GET.get("last_name")

        if first_name:
            queryset = queryset.filter(first_name__icontains = first_name)

        if last_name:
            queryset = queryset.filter(last_name__icontains = last_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_count'] = self.get_queryset().count()
        context['form'] = PolicyholdersSearchForm(self.request.GET)
        context['policyholder_count'] = self.get_queryset().count()
        context['insurance_count'] = Insurance.objects.count()
        context['total_amount'] = Insurance.objects.aggregate(
            Sum('amount')
        )['amount__sum'] or 0

        return context

class PolicyholderDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Policyholder
    template_name = "policyholders/policyholder_detail.html"
    context_object_name = "policyholder"

    def test_func(self):
        policyholder = self.get_object()   #self.get_object() stále čerpá z modelu, ktorý máme definovaný vo views class

        if self. request.user.is_staff:
            return True
        return policyholder.user_id  == self.request.user.id


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        policyholder = self.object
        queryset = policyholder.insurances.all()

        context['insurances'] = queryset
        context['insurance_count'] = queryset.count()    #počíta existujúce poistenia

        return context


class PolicyholderCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Policyholder
    form_class = PolicyholderForm
    template_name = "policyholders/policyholder_create.html"
    success_url = reverse_lazy("policyholder_list")


class PolicyholderUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Policyholder
    form_class = PolicyholderForm
    template_name = "policyholders/policyholder_update.html"
    success_url = "/"

    def get_success_url(self):
        return reverse_lazy(
            "policyholder_detail", kwargs={"pk": self.object.pk}
        )

class PolicyholderDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Policyholder
    template_name = "policyholders/policyholder_delete.html"
    success_url = reverse_lazy("policyholder_list")


"""----------------------------------------------------------"""

"""----------------Vytvorenie CRUD pre poistenia-------------"""
class InsuranceCreateView(LoginRequiredMixin, InsuranceSuccessUrlMixin, CreateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = "policyholders/insurance_create.html"

    def form_valid(self, form):
        """ručné priradenie poistenca ku formuláru"""
        form.instance.policyholder = self.request.user.policyholder
        messages.success(self.request,"Poistenie bolo úspešne vytvorené.")
        return super().form_valid(form)


class InsuranceDetailView(LoginRequiredMixin, UserInsuranceQuerySetMixin, DetailView):
    model = Insurance
    template_name = "policyholders/insurance_detail.html"

class InsuranceDeleteView(LoginRequiredMixin, InsuranceOwnOrStaffMixin, InsuranceSuccessUrlMixin, DeleteView):
    model = Insurance
    template_name = "policyholders/insurance_delete.html"

    def get_success_url(self):
        messages.success(self.request,"Poistenie bolo úspešne vymazane.")
        return super().get_success_url()

class InsuranceUpdateView(LoginRequiredMixin, InsuranceOwnOrStaffMixin, InsuranceSuccessUrlMixin, UpdateView):
    model = Insurance
    form_class = InsuranceForm
    template_name = "policyholders/insurance_update.html"

    def form_valid(self, form):
        messages.success(self.request, "Poistenie bolo úspešne upravené.")
        return super().form_valid(form)


class InsuranceListView(LoginRequiredMixin, UserInsuranceQuerySetMixin, ListView):
    model = Insurance
    template_name = "policyholders/insurance_list.html"
    context_object_name = "insurances"


"""Detail a Update profilu"""
class MyAccountDetailView(LoginRequiredMixin, CurrentPolicyholderMixin, DetailView):
    model = Policyholder
    template_name = 'policyholders/my_account.html'

class MyAccountUpdateView(LoginRequiredMixin, CurrentPolicyholderMixin, UpdateView):
    model = Policyholder
    fields = ['first_name', 'age']
    template_name = 'policyholders/my_account_update.html'
    success_url = reverse_lazy('my_account')

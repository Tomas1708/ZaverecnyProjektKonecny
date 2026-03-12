from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import RegistrationForm, LoginForm
from policyholders.models import Policyholder
from django.contrib.auth.views import LoginView, FormView
from django.views.generic.base import RedirectView


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm

class RegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request,"Registrácia prebehla úspešne.")
        return super().form_valid(form)

class InsuranceRedirectectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_staff:
            return reverse_lazy('insurance_list')
        else:
            return reverse_lazy('policyholder_detail', kwargs={'pk':self.request.user.rpolicyholder.pk})



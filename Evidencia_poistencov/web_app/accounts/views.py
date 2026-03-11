from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from policyholders.models import Policyholder
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Registrácia prebehla úspešne.")
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html',{'form':form})


@login_required
def insurance_redirect(request):
    if request.user.is_staff:
        return redirect('insurance_list')
    else:
        policyholder = request.user.policyholder
        return redirect('policyholder_detail', pk=policyholder.pk)




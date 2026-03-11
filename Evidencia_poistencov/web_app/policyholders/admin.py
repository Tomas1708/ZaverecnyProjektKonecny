from django.contrib import admin
from .forms import PolicyholderForm
from .models import Policyholder, Insurance
# Register your models here.

@admin.register(Policyholder)
class PolicyholderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "age", "phone_number")
    search_fields = ("first_name", "last_name")

@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ("insurance_type", "policyholder","amount")
    list_filter = ("policyholder",)



from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class InsuranceOwnOrStaffMixin(UserPassesTestMixin):

    """Umožňuje bežnému používateľovi upravovať alebo mazať len svoje poistenia.
       Admin/Staff môže upravovať, mazať všetky."""

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(policyholder__user=self.request.user)

    def test_func(self):
        insurance = self.get_object()
        return (
                self.request.user.is_staff or
                insurance.policyholder.user == self.request.user
        )

class UserInsuranceQuerySetMixin:
    """Obmedzuje zobrazenie poistiek na aktuálneho poistenca.
    Admin/staff vidí všetký poistky."""
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_staff:
            return qs
        return qs.filter(
            policyholder__user = self.request.user #prechod cez ForeignKey + OneToOne; aktuálne prihlasený user
        )


class StaffRequiredMixin(UserPassesTestMixin):
    """Umožňuje zmeny len používateľom so staff právami."""
    def test_func(self):
        return self.request.user.is_staff

class InsuranceSuccessUrlMixin:
    """Zabezpečuje presmerovanie na detail poistenca po úspešnom vytvorení alebo aktualizácii poistenia."""
    def get_success_url(self):
        return reverse_lazy(
            "policyholder_detail",
            kwargs={"pk": self.object.policyholder.pk}
        )

class CurrentPolicyholderMixin:
    """Vracia poistenec objekt priradený k aktuálnemu prihlásenému používateľovi. """
    def get_object(self):
        return self.request.user.policyholder
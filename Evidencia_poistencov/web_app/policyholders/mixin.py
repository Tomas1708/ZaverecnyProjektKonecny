from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class InsuranceOwnOrStaffMixin(UserPassesTestMixin):

    """Bežný používateľ môže vymazať len svoje poistenia, cudzí -> 403 Forbidden
       Admin/Staff môže"""

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
    """Bežný user vidí len svoje poistenia, admin/staff vidí všetky"""
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_staff:
            return qs
        return qs.filter(
            policyholder__user = self.request.user #prechod cez ForeignKey + OneToOne; aktuálne prihlasený user
        )


class StaffRequiredMixin(UserPassesTestMixin):
    """metóda umožňuje robiť zmeny len Adminovy"""
    def test_func(self):
        return self.request.user.is_staff

class InsuranceSuccessUrlMixin:
    def get_success_url(self):
        return reverse_lazy(
            "policyholder_detail",
            kwargs={"pk": self.object.policyholder.pk}
        )

class CurrentPolicyholderMixin:
    def get_object(self):
        return self.request.user.policyholder
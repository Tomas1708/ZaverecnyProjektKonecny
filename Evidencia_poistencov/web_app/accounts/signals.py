from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from policyholders.models import Policyholder
@receiver(post_save, sender=User)
def create_policyholder(sender, instance, created, **kwargs):
    if created:
        Policyholder.objects.create(
            user = instance,
            first_name = instance.first_name or instance.username,
            last_name = instance.last_name or "",
            age = 0
        )
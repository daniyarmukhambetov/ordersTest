from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Profile
from .models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

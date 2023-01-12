from django.db import models

from users.models import User


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=16, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")

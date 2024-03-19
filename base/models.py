from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, default='')
    birth_date = models.DateField(default=timezone.now)

    REQUIRED_FIELDS = []

# Comment out models.py line 9 and models.py line 12 and forms.py lines 15-17 before adding superuser
# Uncomment after creating superuser account
    
# Create custom superuser manager to include birthdate as a required field





from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(blank=False, default='', unique=True)
    username = models.CharField(unique=True, max_length=200, null=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    middle_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=False, default='', null=True)


    REQUIRED_FIELDS = []




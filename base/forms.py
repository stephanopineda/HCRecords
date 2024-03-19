from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'first_name', 'middle_name', 'last_name']
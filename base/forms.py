from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'middle_name', 'last_name'
                  , 'birth_date' , 'username' 
                  ]
        
        widgets = {
            'birth_date': DateInput()
        }


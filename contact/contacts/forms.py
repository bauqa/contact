from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
#mektep4

class SignUpForm(UserCreationForm):
    class Meta:
        model = CUser
        fields = ('first_name','last_name','username','email', 'password1', 'password2', )

class ProfileChange(forms.ModelForm):
    class Meta:
        model = CUser
        fields = ('first_name','last_name','username','city','country',
                  'birthday','gender','face','interes')
        widgets = {
            'password':forms.PasswordInput(attrs={'value':""}),
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

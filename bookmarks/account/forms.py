from django import forms
from django.contrib.auth.models import User

# form for th login 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

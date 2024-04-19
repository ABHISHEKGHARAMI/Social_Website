from django import forms
from django.contrib.auth.models import User

# importing the Profile from the model
from .models import Profile

# form for th login 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
# user registration form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    
    # creating the meta class
    class Meta:
        model = User
        fields = ['username','first_name','email']
        
        
    # checking passwords
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords don\'t match')
        return cd['password2']
    
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']
        
        
# form for profile edit
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth','photo']
    
    
    
    

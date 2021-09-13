from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import volentiar

class VolentiarRegistration(forms.ModelForm):
    email= forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = volentiar
        fields = ['firstname','lastname','email','user_name','password1','password2']
class loginForm(forms.ModelForm):
    email= forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = volentiar
        fields = ['email','password1']



from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module
from django.contrib.auth.forms import AuthenticationForm

ModuleFormSet = inlineformset_factory(Course, Module, fields=['title', 'description'], extra=1, can_delete=True)

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder':'username'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'password'}
    ))
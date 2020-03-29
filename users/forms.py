from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from .models import User

class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
            'email': EmailInput(attrs={'placeholder': 'Email'})
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'email', 'is_superuser', 'is_active']
        widgets = {
            'username': TextInput(attrs={'placeholder': 'username'}),
            'email': EmailInput(attrs={'placeholder': 'email'})
        }
        labels = {
            'is_superuser': 'Is Admin'
        }


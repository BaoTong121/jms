from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

from .models import Assets


class AssetsFrom(ModelForm):
    class Meta:
        model = Assets
        fields = '__all__'
        widgets = {
            'hostname': TextInput(attrs={'placeholder': 'Hostname'}),
            'ip': TextInput(attrs={'placeholder': 'IP'}),
            'port': TextInput(attrs={'placeholder': 'Port'}),
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }

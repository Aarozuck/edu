from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'role', 'password1', 'password2', 'address', 'phone')

    address = forms.CharField(max_length=255, required=True)
    phone = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)


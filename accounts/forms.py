from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from .models import User


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")

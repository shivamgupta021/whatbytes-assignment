from django.contrib.auth.views import (
    LoginView,
)
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/home.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


class UserSignUpView(CreateView):
    form_class = UserSignupForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "accounts/login.html"

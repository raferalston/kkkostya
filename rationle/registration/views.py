from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView
# Create your views here.
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from rating.forms import RegisterForm
from django.urls import reverse_lazy
from rating.models import Rating

class ProfileView(DetailView):
    template_name = "registration/profile.html"
    model = User

    def get_object(self):
        return get_object_or_404(User, username=self.request.user.username)

class LoginiView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("main")
class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("main")
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import StoreUserCreationForm
from django.urls import reverse_lazy 

# Create your views here.

class SignUpView(CreateView):
    form_class = StoreUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
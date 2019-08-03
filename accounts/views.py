from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreation

class Register(CreateView):
    form_class = UserCreation
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'



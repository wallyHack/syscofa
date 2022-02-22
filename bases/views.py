from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class Home(LoginRequiredMixin, TemplateView):    
    template_name = 'bases/home.html'
    login_url = '/admin/' # sino esta logeado se redireccona al admin
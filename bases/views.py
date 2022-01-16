from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = 'bases/home.html'
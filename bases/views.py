from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic.base import TemplateView

class Home(LoginRequiredMixin, TemplateView):    
    template_name = 'bases/home.html'
    login_url = 'bases:login' # sino esta logeado se redireccoona al admin
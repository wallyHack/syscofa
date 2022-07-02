
from logging import raiseExceptions
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from re import template
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from django.views import generic
from django.views.generic.base import TemplateView

class Sin_Privilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raiseExceptions = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser

        # si el usuario es válido, se muestra la vista sin privilegios
        if not self.request.user == AnonymousUser():
            self.login_url = "bases:sin_privilegios"

        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin, TemplateView):    
    template_name = 'bases/home.html'
    login_url = 'bases:login' # sino esta logeado se redireccona al admin

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    template_name = "bases/sin_privilegios.html"

class VistaBaseCreate(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    context_object_name = "obj"
    success_message = "Registro Agregado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user 
        return super().form_valid(form)

class VistaBaseEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    context_object_name = "obj"
    success_message = "Registro Actualizado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id 
        return super().form_valid(form)
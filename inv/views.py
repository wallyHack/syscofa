from pyexpat import model
from re import template
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Categoria
from .forms import CategoriaForm

# Create your views here.
class CategoriaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase que lista las categorías"""
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class CategoriaNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para crear una nueva categoría"""
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class =  CategoriaForm #formulario a utilizar
    success_url = reverse_lazy("inv:categoria_list") #redireccionamos a la lista de categorías
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):    
    """ vista basada en clase para editar y actualizar una categoría"""
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class =  CategoriaForm #formulario a utilizar
    success_url = reverse_lazy("inv:categoria_list") #redireccionamos a la lista de categorías
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)
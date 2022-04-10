from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Categoria, SubCategoria, Marca
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm

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
    """ vista basada en clase para editar y/o actualizar una categoría"""
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class =  CategoriaForm #formulario a utilizar
    success_url = reverse_lazy("inv:categoria_list") #redireccionamos a la lista de categorías
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.edit.DeleteView):
    """ vista basada en clase para eliminar una categoría"""
    model = Categoria
    template_name = "inv/categoria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")

class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase que lista las subcategorías"""
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para crear una nueva subcategoría"""
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class =  SubCategoriaForm #formulario a utilizar
    success_url = reverse_lazy("inv:subcategoria_list") #redireccionamos a la lista de subcategorías
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):    
    """ vista basada en clase para editar y/o actualizar una subcategoría"""
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class =  SubCategoriaForm #formulario a utilizar
    success_url = reverse_lazy("inv:subcategoria_list") #redireccionamos a la lista de subcategorías
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)

class SubCategoriaDel(LoginRequiredMixin, generic.edit.DeleteView):
    """ vista basada en clase para eliminar una subcategoría"""
    model = SubCategoria
    template_name = "inv/catalogos_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")

class MarcaView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase que lista las marcas"""
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class MarcaNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para crear una nueva marca"""
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class =  MarcaForm #formulario a utilizar
    success_url = reverse_lazy("inv:marca_list") #redireccionamos a la lista de marcas
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):    
    """ vista basada en clase para editar y/o actualizar una marca"""
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class =  MarcaForm #formulario a utilizar
    success_url = reverse_lazy("inv:marca_list") #redireccionamos a la lista de marcas
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)

def marca_inactivar(request, id):
    """ vista que inactiva una marca"""
    marca = Marca.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/marca_inactivar.html"

    if not marca:
        return redirect("inv:marca_list")

    if request.method == 'GET':
        contexto = {'obj': marca}

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        return redirect('inv:marca_list')

    return render(request, template_name, contexto)
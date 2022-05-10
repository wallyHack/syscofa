from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm
from bases.views import Sin_Privilegios

# Create your views here.
class CategoriaView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase que lista las categorías"""
    permission_required = 'inv.view_categoria'
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"

class CategoriaNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    """ vista basada en clase para crear una nueva categoría"""
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class =  CategoriaForm #formulario a utilizar
    success_url = reverse_lazy("inv:categoria_list") #redireccionamos a la lista de categorías
    success_message = "Categoría creada satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class CategoriaEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):    
    """ vista basada en clase para editar y/o actualizar una categoría"""
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class =  CategoriaForm #formulario a utilizar
    success_url = reverse_lazy("inv:categoria_list") #redireccionamos a la lista de categorías
    success_message = "Categoría actualizada satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)

class CategoriaDel(LoginRequiredMixin, generic.edit.DeleteView):
    """ vista basada en clase para eliminar una categoría"""
    model = Categoria
    template_name = "inv/categoria_del.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")

class SubCategoriaView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase que lista las subcategorías"""
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"

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

class MarcaView(Sin_Privilegios, generic.ListView):
    """ vista basada en clase que lista las marcas"""
    permission_required = 'inv.view_marca'
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
        messages.success (request, 'Marca Inactivada')
        return redirect('inv:marca_list')

    return render(request, template_name, contexto)

class UMView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase que lista las unidades de medida"""
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class UMNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para crear una nueva unidad de medida"""
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class =  UMForm #formulario a utilizar
    success_url = reverse_lazy("inv:um_list") #redireccionamos a la lista de unidades de medida
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class UMEdit(LoginRequiredMixin, generic.UpdateView):    
    """ vista basada en clase para editar y/o actualizar una unidad de medida"""
    model = UnidadMedida
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class =  UMForm #formulario a utilizar
    success_url = reverse_lazy("inv:um_list") #redireccionamos a la lista de unidades de medida
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)

def um_inactivar(request, id):
    """ vista que inactiva una unidad de medida"""
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/um_inactivar.html"

    if not um:
        return redirect("inv:um_list")

    if request.method == 'GET':
        contexto = {'obj': um}

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect('inv:um_list')

    return render(request, template_name, contexto)

class ProductoView(LoginRequiredMixin, generic.ListView):
    """ vista basada en clase que lista los productos"""
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProductoNew(LoginRequiredMixin, generic.CreateView):
    """ vista basada en clase para crear una nuevo producto"""
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class =  ProductoForm #formulario a utilizar
    success_url = reverse_lazy("inv:producto_list") #redireccionamos a la lista de productos
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):    
    """ vista basada en clase para editar y/o actualizar un producto"""
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class =  ProductoForm #formulario a utilizar
    success_url = reverse_lazy("inv:producto_list") #redireccionamos a la lista de productos
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)

def producto_inactivar(request, id):
    """ vista que inactiva una producto"""
    producto = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name="inv/producto_inactivar.html"

    if not producto:
        return redirect("inv:producto_list")

    if request.method == 'GET':
        contexto = {'obj': producto}

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        return redirect('inv:producto_list')

    return render(request, template_name, contexto)
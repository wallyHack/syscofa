from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Proveedor
from .forms import ProveedorForm

# Create your views here.
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class =  ProveedorForm #formulario a utilizar
    success_url = reverse_lazy("cmp:proveedor_list") #redireccionamos a la lista de proveedores
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):    
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class =  ProveedorForm #formulario a utilizar
    success_url = reverse_lazy("cmp:proveedor_list") #redireccionamos a la lista de proveedores
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)
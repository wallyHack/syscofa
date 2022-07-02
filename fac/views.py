from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from bases.views import Sin_Privilegios
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
class ClienteView(Sin_Privilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required = "fac/view_cliente"

class ClienteNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    model = Cliente
    template_name = "fac/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    permission_required = 'fac.add_cliente'
    success_message = "Cliente creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class ClienteEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
    model = Cliente
    template_name = "fac/cliente_form.html"
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list") 
    permission_required = 'fac.change_cliente'
    success_message = "Cliente actualizado satisfactoriamente"

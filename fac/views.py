from django.shortcuts import render
from django.views import generic

from bases.views import Sin_Privilegios
from .models import Cliente

# Create your views here.
class ClienteView(Sin_Privilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required = "fac/view_cliente"
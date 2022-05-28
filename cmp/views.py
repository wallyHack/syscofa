from re import template
from xmlrpc.client import DateTime
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
import datetime
from django.http import HttpResponse

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
import json

from django.contrib.auth.decorators import login_required, permission_required

from .models import Proveedor, ComprasEnc, CompraDet
from .forms import ComprasEncForm
from inv.models import Producto
from .forms import ProveedorForm
from bases.views import Sin_Privilegios

# Create your views here.
class ProveedorView(Sin_Privilegios, generic.ListView):
    model = Proveedor
    template_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    permission_required = 'cmp.view_proveedor'

class ProveedorNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class =  ProveedorForm #formulario a utilizar
    success_url = reverse_lazy("cmp:proveedor_list") #redireccionamos a la lista de proveedores
    permission_required = 'cmp.add_proveedor'
    success_message = "Proveedor creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):    
    model = Proveedor
    template_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class =  ProveedorForm #formulario a utilizar
    success_url = reverse_lazy("cmp:proveedor_list") #redireccionamos a la lista de proveedores
    permission_required = 'cmp.change_proveedor'
    success_message = "Proveedor actualizado satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id #ubicamos al usuario que modificó el formulario
        return super().form_valid(form)

@login_required(login_url='/login/') #debo estar logeado
@permission_required('inv.change_marca', login_url='bases:sin_privilegios') # y tener permiso para modificar
def inactivar_proveedor(request, id):
    template_name = "cmp/inactivar_proveedor.html"
    contexto = {}

    proveedor = Proveedor.objects.filter(pk=id).first()
    if not proveedor:
        return HttpResponse('Proveedor no existe' + str(id))

    if request.method == 'GET':
        contexto = {'obj': proveedor}

    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        contexto = {'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request, template_name, contexto)

class ComprasView(Sin_Privilegios, generic.ListView):
    model = ComprasEnc
    template_name = "cmp/compras_list.html"
    context_object_name = "obj"
    permission_required = 'cmp.view_comprasenc'

@login_required(login_url='/login/')
@permission_required('cmp:view_comprasenc', login_url='bases:sin_privilegios')
def compras(request, compra_id=None):
    template_name = 'cmp/compras.html'
    prod = Producto.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    if request.method == 'GET':
        form_compras = ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = CompraDet.objects.filter(compras=enc)
            fecha_compra = DateTime.date.isoformat(enc.fecha_compra)
            fecha_factura = DateTime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra': fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total': enc.total
            }

            form_compras = ComprasEncForm(e)
        else:
            det=None

        contexto = {'productos': prod, 'encabezado':enc, 'detalle':det, 'form_enc':form_compras}

        return render(request, template_name, contexto)



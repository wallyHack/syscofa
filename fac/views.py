from multiprocessing import context
from operator import inv
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from datetime import datetime

from bases.views import Sin_Privilegios, VistaBaseCreate, VistaBaseEdit
from .models import Cliente, FacturaDet, FacturaEnc
from .forms import ClienteForm
from inv import views as inv

# Create your views here.
class ClienteView(Sin_Privilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required = "fac/view_cliente"

class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    permission_required = 'fac.add_cliente'

class ClienteEdit(VistaBaseEdit):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list") 
    permission_required = 'fac.change_cliente'

@login_required(login_url='/login/') #necesitamos estar logeados
@permission_required("fac:change_cliente", login_url='/login/') #permiso requerido
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method == "POST":
        if cliente: # si se creo el cliente
            #si cliente esta en true se cambia a false o viceversa
            cliente.estado = not cliente.estado 
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")

    return HttpResponse("FAIL")
    
class FacturaView(Sin_Privilegios, generic.ListView):
    model = FacturaEnc
    template_name = "fac/factura_list.html"
    context_object_name = "obj"
    permission_required = 'fac.view_facturaenc'

@login_required(login_url='/login/') #necesitamos estar logeados
@permission_required("fac:change_facturaenc", login_url='bases:sin_privilegios') #permiso requerido
def facturas(request, id=None):
    template_name = "fac/facturas.html"
    encabezado = {
        'fecha': datetime.today()
    }
    detalle = {}
    clientes = Cliente.objects.filter(estado=True)

    if request.method == "GET":
        enc = FacturaEnc.objects.filter(pk=id).first()
        if not enc:
            encabezado = {
                'id': 0,
                'fecha': datetime.today,
                'cliente': 0,
                'sub_total': 0.00,
                'descuento': 0.00,
                'total': 0.00
            }
            detalle = None
        else:
            encabezado = {
                'id': enc.id,
                'fecha': enc.fecha,
                'cliente': enc.cliente,
                'sub_total': enc.sub_total,
                'descuento': enc.decuento,
                'total': enc.total
            }
            detalle = FacturaDet.objects.filter(factura=enc)
        

    contexto = {"enc":encabezado, "det":detalle, "clientes":clientes}
    
    return render(request, template_name, contexto)

class ProductoView(inv.ProductoView):
    template_name = "fac/buscar_producto.html"


# class ClienteNew(SuccessMessageMixin, Sin_Privilegios, generic.CreateView):
#     model = Cliente
#     template_name = "fac/cliente_form.html"
#     context_object_name = "obj"
#     form_class = ClienteForm
#     success_url = reverse_lazy('fac:cliente_list')
#     permission_required = 'fac.add_cliente'
#     success_message = "Cliente creado satisfactoriamente"

#     def form_valid(self, form):
#         form.instance.uc = self.request.user #ubicamos al usuario que creo el formulario
#         return super().form_valid(form)

# class ClienteEdit(SuccessMessageMixin, Sin_Privilegios, generic.UpdateView):
#     model = Cliente
#     template_name = "fac/cliente_form.html"
#     context_object_name = "obj"
#     form_class = ClienteForm
#     success_url = reverse_lazy("fac:cliente_list") 
#     permission_required = 'fac.change_cliente'
#     success_message = "Cliente actualizado satisfactoriamente"

#     def form_valid(self, form):
#         form.instance.um = self.request.user.id #ubicamos al usuario que editó el formulario
#         return super().form_valid(form)

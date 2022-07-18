from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import ProductoSerializer
from inv.models import Producto
from django.db.models import Q

# Create your views here.
class ProductoList(APIView):
    """ obtenemos una lista de productos"""
    def get(self, request):
        prod = Producto.objects.all()
        #serializamos la lista de productos
        data = ProductoSerializer(prod, many=True).data 
        return Response(data)

class ProductoDetalle(APIView):
    def get(self, request, codigo):
        # el objeto Q es para filtrar 2 elementos con el condicional o
        prod = get_object_or_404(Producto, Q(codigo=codigo) | Q(codigo_barra=codigo))
        #serializamos el producto
        data = ProductoSerializer(prod).data
        return Response(data)

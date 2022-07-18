from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import ProductoSerializer
from inv.models import Producto

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
        prod = get_object_or_404(Producto, codigo=codigo)
        #serializamos el producto
        data = ProductoSerializer(prod).data
        return Response(data)

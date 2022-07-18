
from rest_framework import serializers
from inv.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """ clase que transforma el data del modelo en json/xml para la api """

    class Meta:
        model = Producto
        fields = '__all__'


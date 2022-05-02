
from django.urls import path, include

from .views import ProveedorView, ProveedorNew, ProveedorEdit, inactivar_proveedor

urlpatterns = [
    path('proveedores/', ProveedorView.as_view(), name="proveedor_list"),
    path("proveedores/new", ProveedorNew.as_view(), name="proveedor_new"),
    path("proveedores/edit/<int:pk>", ProveedorEdit.as_view(), name="proveedor_edit"),
    path("proveedores/inactivar/<int:id>", inactivar_proveedor, name="proveedor_inactivar"),
]
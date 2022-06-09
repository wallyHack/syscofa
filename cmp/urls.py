
from django.urls import path, include

from .views import ProveedorView, ProveedorNew, ProveedorEdit, inactivar_proveedor, \
    ComprasView, compras

urlpatterns = [
    path("proveedores/", ProveedorView.as_view(), name="proveedor_list"),
    path("proveedores/new", ProveedorNew.as_view(), name="proveedor_new"),
    path("proveedores/edit/<int:pk>", ProveedorEdit.as_view(), name="proveedor_edit"),
    path("proveedores/inactivar/<int:id>", inactivar_proveedor, name="proveedor_inactivar"),

    path("compras/", ComprasView.as_view(), name="compras_list"),
    path("compras/new", compras, name="compras_new"),
    path("compras/edit/<int:compra_id>", compras, name="compras_edit")
]

from django.urls import path, include

from .views import ProveedorView, ProveedorNew, ProveedorEdit

urlpatterns = [
    path('proveedores/', ProveedorView.as_view(), name="proveedor_list"),
    path("proveedores/", ProveedorNew.as_view(), name="proveedor_new"),
    path("proveedores/", ProveedorEdit.as_view(), name="proveedor_edit"),
]
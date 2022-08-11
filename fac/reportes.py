
from django.shortcuts import render
from django.utils.dateparse import parse_date
from datetime import timedelta

from .models import FacturaEnc, FacturaDet

# vistas concernientes a las facturas

def imprimir_factura_recibo(request, id):
    template_name = "fac/facturas_one.html"

    enc = FacturaEnc.objects.get(id=id)
    det = FacturaDet.objects.filter(factura=id)

    context = {
        'request': request,
        'enc': enc,
        'det': det
    }

    return render(request, template_name, context)

def imprimir_factura_list(request, f1, f2):
    template_name = "fac/facturas_print_all.html"

    # convertimos las fechas que vienen en formato de texto a fecha
    f1 = parse_date(f1)
    f2 = parse_date(f2)
    f2 = f2 + timedelta(days=1) # sumamos 1 dia a la fecha 

    # consulta de rango de fechas
    enc = FacturaEnc.objects.filter(fecha__gte=f1, fecha__lt=f2)
    f2 = f2 - timedelta(days=1) # restamos 1 dia a la fecha 

    context = {
        'request': request,
        'f1': f1,
        'f2': f2,
        'enc': enc
    }

    return render(request, template_name, context)
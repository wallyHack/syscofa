import imp
import os
from re import template
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from pytz import timezone
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import ComprasEnc, ComprasDet
from django.utils import timezone

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

#muestra todas las compras
def reporte_compras(request):
    template_path = 'cmp/compras_print_all.html'
    today = timezone.now() #fecha actual

    compras = ComprasEnc.objects.all() #obtenemos todas las compras
    context = {
        'obj': compras,
        'today': today,
        'request': request
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=todas_compras.pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    #creamos el pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#muestra una compra específica
def imprimir_compra(request, compra_id):
    template_path = 'cmp/compras_print_one.html'
    today = timezone.now() #fecha actual

    enc = ComprasEnc.objects.filter(id=compra_id).first() #obtenemos la compra
    if enc: #si hay compra
        detalle =  ComprasDet.objects.filter(compra_id=compra_id) #busco su detalle(caracteristicas)
    else:
        detalle = {}

    #contexto que se renderiza a la plantilla
    context = {
        'detalle': detalle,
        'encabezado': enc,
        'today': today,
        'request': request
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="una_compra.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

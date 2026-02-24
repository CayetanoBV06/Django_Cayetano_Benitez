from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def productos(request):
    doc_externo = open("/home/usuario/Escritorio/proyecto2/proyecto2/proyecto2/plantillas/plantilla.html")

    mensaje="Estas en la pantalla de productos"
    planti=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"mensaje":mensaje})

    documento=planti.render(ctx)

    return HttpResponse(documento)

def altas_productos(request):
#   secciones = Secciones.objects.all()
#   return render(request, "subplantillas_productos/altas_productos.html", {"secciones": secciones})
    return render(request, "subplantillas_productos/altas_productos.html")


def listado_productos(request):
   # productos = Productos.objects.all()
    #secciones = Secciones.objects.all()
    #return render(request, "subplantillas_productos/listado_productos.html", {"productos": productos})
    return render(request, "subplantillas_productos/listado_productos.html")
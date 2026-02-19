from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.template import Template, Context

def secciones(request):
    doc_externo = open("/home/usuario/Escritorio/proyecto2/proyecto2/proyecto2/plantillas/plantilla.html")

    mensaje="Estas en la pantalla de secciones"
    planti=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"mensaje":mensaje})

    documento=planti.render(ctx)

    return HttpResponse(documento)
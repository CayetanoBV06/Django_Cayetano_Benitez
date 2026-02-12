from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    doc_externo = open("/home/usuario/Escritorio/proyecto2/proyecto2/proyecto2/plantillas/plantilla.html")

    nombre="Cayetano"
    planti=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":nombre})

    documento=planti.render(ctx)

    return HttpResponse(documento)
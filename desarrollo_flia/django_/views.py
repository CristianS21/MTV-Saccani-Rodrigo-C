from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from app_flia.models import Familiar
from django.template import loader


def bienvenida (request):
    return HttpResponse ("*** Bienvenidos al desafío Entregable Número 6 *** ")


def hoy (request):
    dia = datetime.now()
    texto_dia= f"Hoy es: {dia}"
    return HttpResponse (texto_dia)


def template_1 (request):
    consulta = Familiar.objects.all()

    diccionario = {"familiares" : consulta}
    plantilla1= loader.get_template("C:/Users/Thinkpad T440p/OneDrive/Escritorio/Familia/desarrollo_flia/Plantillas/template_1.html")
    documento_html= plantilla1.render (diccionario)
         
    return HttpResponse (documento_html)
    


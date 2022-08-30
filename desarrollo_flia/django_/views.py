from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
from app_flia.models import Familiar
from django.template import loader



def template_1 (request):
    consulta = Familiar.objects.all()

    diccionario = {"familiares" : consulta}
    plantilla1= loader.get_template("template_1.html")
    documento_html= plantilla1.render (diccionario)
         
    return HttpResponse (documento_html)
    


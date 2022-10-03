import email
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import family

# Create your views here.
def crear_familia (request):
    template = loader.get_template("template1.html")
    
    fran = family(nombre="Franco", integrante="Hijo", email="franco@coder.com", nacimiento= '2002-01-03')
    martina = family(nombre="Martina", integrante="madre", email="martina@coder.com", nacimiento= '1982-10-02')
    lucas = family(nombre="Lucas", integrante="hermano", email="lucas@coder.com", nacimiento= '2008-11-10')
    
    dict_de_contexto = {
        "fran": fran.nombre,
        "martina": martina.nombre,
        "lucas":  lucas.nombre,
       
    
    }
    text = template.render(dict_de_contexto)
    
    
    return HttpResponse(text)
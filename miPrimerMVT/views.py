from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppFamilia.models import Familia
import datetime

def miFamilia(request):
    
    # USANDO LOADER
    # diccionario = {}
    # plantillas = loader.get_template('template.html')
    # documento = plantillas.render(diccionario)

    # return HttpResponse(documento)
    fechaNac1 = datetime.date(1957,6,27)
    familiar1 = Familia(titulo="Madre", cantHuesos=6821, fechaNac=fechaNac1)
    familiar1.save()
    
    fechaNac2 = datetime.date(1870,9,1)
    familiar2 = Familia(titulo="Perro", cantHuesos=3, fechaNac=fechaNac2)
    familiar2.save()
    
    fechaNac3 = datetime.date(2021,6,15)
    familiar3 = Familia(titulo="Hermano", cantHuesos=25910, fechaNac=fechaNac3)
    familiar3.save()
    
    context = {"familiar1":familiar1,"familiar2":familiar2,"familiar3":familiar3}

    # documentoDeTexto = f'Título ==> {familiar1.titulo} | Cantidad de Huesos ==> {familiar1.cantHuesos} | Fecha de Nacimiento ==> {familiar1.fechaNac}\n'
    # documentoDeTexto2 = f'\nTítulo ==> {familiar2.titulo} | Cantidad de Huesos ==> {familiar2.cantHuesos} | Fecha de Nacimiento ==> {familiar2.fechaNac}'
    
    # print(type(familiar1.fechaNac))
    # return HttpResponse(documentoDeTexto+documentoDeTexto2)
    return render(request,'template.html', context)

# .strftime("%Y-%m-%d")

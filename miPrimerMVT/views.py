from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppFamilia.models import Familia
import datetime

def miFamilia(request):
    
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

    return render(request,'template.html', context)

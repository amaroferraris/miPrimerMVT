from django.db import models
from datetime import datetime, date

# Create your models here.
class Familia(models.Model):
    titulo = models.CharField(max_length=10)
    cantHuesos = models.IntegerField()
    fechaNac = models.DateField()
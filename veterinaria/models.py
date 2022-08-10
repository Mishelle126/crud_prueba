from django.db import models

# Create your models here.
class Vete(models.Model):
    dueño = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mascota = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    agencia = models.CharField(max_length=100)
    

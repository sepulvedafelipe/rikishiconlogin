from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=20, blank=True)
    nombre = models.CharField(max_length=30, blank=True) 
    apellido = models.CharField(max_length=30, blank=True)
    telefono= models.CharField(max_length=20, blank=True)
    correo = models.CharField(max_length=30, blank=True)
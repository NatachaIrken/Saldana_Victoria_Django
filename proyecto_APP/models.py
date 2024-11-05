from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono_contacto = models.CharField(max_length=20)
    fecha_seminario = models.DateField()
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=100)
    institucion_perteneciente = models.CharField(max_length=100, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

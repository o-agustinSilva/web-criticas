from django.db import models

# Create your models here.
class Director(models.Model):
    nombre          = models.CharField(max_length=50)
    nacionalidad    = models.CharField(max_length=30)
    # foto 
    anio_nacimiento = models.IntegerField(default = None)
    resumen_bibliografico = models.CharField(max_length=300)
    # Declarar clave foranea
    

class Actor(models.Model):
    pass

class Pelicula(models.Model):
    pass


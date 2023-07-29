from django.db import models
from faker import Faker # CMD: pip install faker 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
import random

# ----------- Clases -----------
class Director(models.Model):

    # Datos del director
    nombre                  = models.CharField(max_length=50)
    nacionalidad            = models.CharField(max_length=30)
    foto                    = models.ImageField(upload_to='directores', blank=True, null=True)
    anio_nacimiento         = models.IntegerField(default = None)
    resumen_bibliografico   = models.CharField(max_length=3000)

    def __str__(self):
        return self.nombre
    

class Actor(models.Model):

    # Datos del actor
    nombre                  = models.CharField(max_length=50)
    nacionalidad            = models.CharField(max_length=30)
    foto                    = models.ImageField(upload_to='actores', blank=True, null=True)
    anio_nacimiento         = models.IntegerField(default = None)
    resumen_bibliografico   = models.CharField(max_length=3000)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):

    # Choices
    CATEGORIAS_PELICULAS = [
                                ("ACCION", 'Accion'),
                                ("COMEDIA", 'Comedia'), 
                                ("DRAMA", 'Drama'), 
                                ("AVENTURA", 'Aventura'),
                                ("TERROR", 'Terror'),
                                ("CIENCIA FICCION", "Ciencia ficción")
                           ]   

    # Datos de la pelicula
    anio_pelicula   = models.IntegerField(default = None)
    puntaje         = models.IntegerField(default = None)
    foto            = models.ImageField(upload_to='imagenes_peliculas/', blank=True, null=True)
    nombre          = models.CharField(max_length = 70)
    resumen         = models.CharField(max_length = 3000)
    critica_mono    = models.CharField(max_length = 3000, default = '')
    categoria       = models.CharField(
                                        max_length  = 20, 
                                        choices     = CATEGORIAS_PELICULAS,
                                        default     = "ACCION",
                                      )  

    # Claves foráneas
    director        = models.ForeignKey(Director, on_delete=models.CASCADE)
    actores         = models.ManyToManyField(Actor)

    def __str__(self):
        return self.nombre

class Critica(models.Model):
    
    ESTADOS_CRITICAS = [
        ("APROBADO", 'Aprobado'),  
        ("RECHAZADO", 'Rechazado'),
        ("PENDIENTE", 'Pendiente')
    ]
    
    #Datos de las criticas
    critica     = models.CharField(max_length = 1000)
    nombre      = models.CharField(max_length = 70, default = 'None')
    correo      = models.CharField(max_length=35, default='None')
    puntaje     = models.IntegerField(default = None) 
    estado      = models.CharField(
                                    max_length=9,
                                    choices=ESTADOS_CRITICAS,
                                    default="PENDIENTE"
                                  )
    pelicula    = models.ForeignKey(Pelicula, on_delete=models.CASCADE)


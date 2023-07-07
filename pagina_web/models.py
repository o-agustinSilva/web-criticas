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
    resumen_bibliografico   = models.CharField(max_length=300)
    

class Actor(models.Model):

    # Datos del actor
    nombre                  = models.CharField(max_length=50)
    nacionalidad            = models.CharField(max_length=30)
    foto                    = models.ImageField(upload_to='actores', blank=True, null=True)
    anio_nacimiento         = models.IntegerField(default = None)
    resumen_bibliografico   = models.CharField(max_length=300)

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
    resumen         = models.CharField(max_length = 1000)
    categoria       = models.CharField(
                                        max_length  = 20, 
                                        choices     = CATEGORIAS_PELICULAS,
                                        default     = "ACCION",
                                      )  

    # Claves foráneas
    director        = models.ForeignKey(Director, on_delete=models.CASCADE)
    actores         = models.ManyToManyField(Actor)

class Critica(models.Model):
    
    #Datos de las criticas
    critica     = models.CharField(max_length = 1000)
    nombre      = models.CharField(max_length = 70, default = 'None')
    correo      = models.CharField(max_length=35, default='None')
    estado      = models.CharField(max_length=20, default = None)
    puntaje     = models.IntegerField(default = None) 
    pelicula    = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

'''
# ----------- Managers -----------
class DirectorManager(models.Manager):
    def crear_nombre(self):
        faker   = Faker()
        nombre  = faker.name()

        return nombre
  
    def crear_nacionalidad(self):
        faker           = Faker()
        nacionalidad    = faker.country()

        return nacionalidad
    
    def crear_anio(self):
        anio = random.randint(1930, 2023)
        return anio
       
    def crear_director(self, cantidad):
        for i in range(cantidad):
            self.create(nombre= self.crear_nombre(), nacionalidad = self.crear_nacionalidad(), anio_nacimiento = self.crear_anio())
'''
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

class Usuario(models.Model):

    # Choices
    ROLES_USUARIOS = [
                        ("USUARIO", "Usuario"),
                        ("ADMINISTRADOR", "Administrador"),
                     ] 

    # Datos de los usuarios
    usuario     = models.CharField(max_length = 15)
    contrasenia = models.CharField(max_length = 20)
    rol         = models.CharField(
                                    max_length  = 13,
                                    choices     = ROLES_USUARIOS,
                                    default     = "USUARIO",
                                  )
    
    def set_password(self, raw_password):
        # Lógica para establecer y almacenar la contraseña de manera segura
        self.contrasenia = make_password(raw_password)

    def check_password(self, raw_password):
        # Lógica para verificar la contraseña ingresada por el usuario
        return check_password(raw_password, self.contrasenia)
    
class Critica(models.Model):
    
    #Datos de las criticas
    critica     = models.CharField(max_length = 1000)
    valoracion  = models.IntegerField(default = None)
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE)
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
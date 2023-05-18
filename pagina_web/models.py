from django.db import models
from faker import Faker # CMD: pip install faker 

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

    # Datos de la pelicula
    nombre          = models.CharField(max_length=70)
    resumen         = models.CharField(max_length=1000)
    anio_pelicula   = models.IntegerField(default = None)

    # Claves foráneas
    director        = models.ForeignKey(Director, on_delete=models.CASCADE)
    actores         = models.ManyToManyField(Actor)


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
       
    def crear_autor(self, cantidad):
        for i in range(cantidad):
            self.create(nombre="Autor " + str(i), nacionalidad = self.crear_nacionalidad(), fecha_nacimiento = self.crear_fecha(i))
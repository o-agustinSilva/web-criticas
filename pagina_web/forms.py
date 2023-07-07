from django import forms
from pagina_web.models import *

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('anio_pelicula', 'puntaje', 'foto', 'nombre', 'resumen', 'categoria', 'director', 'actores')


class CriticaForm(forms.ModelForm):
    class Meta:
        model = Critica
        fields = ['critica', 'correo', 'nombre', 'estado', 'puntaje', 'pelicula']

from django import forms
from pagina_web.models import *
from django.core.validators import MinValueValidator, MaxValueValidator

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ('anio_pelicula', 'puntaje', 'foto', 'nombre', 'resumen', 'categoria', 'director', 'actores')


class CriticaForm(forms.ModelForm):
    puntaje = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    
    class Meta:
        model = Critica
        fields = ['critica', 'correo', 'nombre', 'puntaje']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].initial = ''
        self.fields['correo'].initial = ''
        self.fields['critica'].initial = ''
        self.fields['puntaje'].initial = ''



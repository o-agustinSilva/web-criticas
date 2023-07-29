from django.contrib import admin
from django.forms import ModelForm, Textarea
from django.db.models import CharField
from .models import Director, Actor, Pelicula, Critica


class DirectorAdmin(admin.ModelAdmin):
    list_display    = ('nombre', 'nacionalidad', 'anio_nacimiento')
    search_fields   = ('nombre', 'nacionalidad')


class ActorAdmin(admin.ModelAdmin):
    list_display    = ('nombre', 'nacionalidad', 'anio_nacimiento')
    search_fields   = ('nombre', 'nacionalidad')


class PeliculaForm(ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'
        widgets = {
            'resumen': Textarea(attrs={'rows': 10, 'cols': 80}),
            'critica_mono': Textarea(attrs={'rows': 10, 'cols':80}),
        }

class PeliculaAdmin(admin.ModelAdmin):
    list_display        = ('nombre', 'anio_pelicula', 'categoria', 'director')
    list_filter         = ('categoria', 'anio_pelicula')
    search_fields       = ('nombre', 'resumen', 'director__nombre', 'actores__nombre')
    filter_horizontal   = ('actores',)
    form                = PeliculaForm


# Aprobnar o desaprobar una critica
class CriticaAdmin(admin.ModelAdmin):
    list_display = ('critica', 'nombre', 'correo', 'estado', 'puntaje', 'pelicula')
    list_filter = ('estado', 'puntaje')
    search_fields = ('nombre', 'correo', 'pelicula__nombre')
    actions = ['aprobar_criticas', 'rechazar_criticas', 'eliminar_criticas']

    def has_delete_permission(self, request, obj=None):
        # Allow delete permission for all users
        return True

    def aprobar_criticas(self, request, queryset):
        # Logic to approve the selected criticas
        queryset.update(estado='Aprobada')

    def rechazar_criticas(self, request, queryset):
        # Logic to reject the selected criticas
        queryset.update(estado='Rechazada')

    def eliminar_criticas(self, request, queryset):
        # Logic to delete the selected criticas
        queryset.delete()

    eliminar_criticas.short_description = "Eliminar criticas"


admin.site.register(Critica, CriticaAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)

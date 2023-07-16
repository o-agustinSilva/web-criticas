from typing import Any, Dict
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView
from pagina_web.models import *
from django.shortcuts import render, redirect
from pagina_web.forms import *
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
class Inicio(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
      context = super().get_context_data(**kwargs)
      return context
    
    def get(self, request, *args, **kwargs):
        peliculas = Pelicula.objects.all()

        context = {
            'peliculas': peliculas
        }

        # Peliculas del primer carousel (El señor de los anillos)
        peliculas_recomendadas_uno = Pelicula.objects.filter(Q(nombre__icontains='el señor de los anillos') | Q(nombre__icontains='el hobbit'))
        context['peliculas_primer_carousel'] = peliculas_recomendadas_uno

        # Peliculas del segundo carousel (Star Wars)
        peliculas_recomendadas_dos = Pelicula.objects.filter(Q(nombre__icontains='star wars'))
        context['peliculas_segundo_carousel'] = peliculas_recomendadas_dos

        # Peliculas del tercer carousel (Harry Potter)
        peliculas_recomendadas_tres = Pelicula.objects.filter(Q(nombre__icontains='harry potter'))
        context['peliculas_tercer_carousel'] = peliculas_recomendadas_tres

        # Obtener las 6 películas con mejor puntaje
        peliculas_mejor_puntaje = Pelicula.objects.order_by('-puntaje')[:6]
        context['peliculas_mejor_puntaje'] = peliculas_mejor_puntaje
        
        return render(request, self.template_name, context)

class Detalle_Pelicula(TemplateView):
    template_name = 'detalle_pelicula.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        try:
            identificador = self.kwargs['id']

            # Busco la pelicula por id
            pelicula = Pelicula.objects.all().get(id=identificador)
        except Pelicula.DoesNotExist:
            raise Http404

        # Paso la pelicula al template
        context['pelicula'] = pelicula

        # Pasar la función get_range al contexto
        puntaje = []
        for i in range(0, pelicula.puntaje):
            puntaje.append('a')
        for i in range(pelicula.puntaje, 5):
            puntaje.append('b')
        
        context['puntaje'] = puntaje

        # Obtener los actores asociados a la película
        actores = Actor.objects.filter(pelicula=pelicula)
        context['actores'] = actores

        # Obtener los actores asociados a la película
        director = Director.objects.get(pelicula=pelicula)
        context['director'] = director

        # Obtener las críticas asociadas a la película
        criticas = Critica.objects.filter(pelicula=pelicula, estado="APROBADO")
        context['criticas'] = criticas

        # Inicializar el formulario de crítica
        form = CriticaForm()
        context['form'] = form

        return context

    def post(self, request, *args, **kwargs):
        id_pelicula = self.kwargs['id']

        form = CriticaForm(request.POST)
        if form.is_valid():
            crítica = form.save(commit=False)
            crítica.pelicula_id = id_pelicula
            crítica.save()
            return redirect('PeliculaView', id=id_pelicula)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class Detalle_Actor(TemplateView):
    template_name = 'detalle-actor.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        try:
            identificador = self.kwargs['id_actor']

            # Busco la pelicula por id
            actor = Actor.objects.get(id=identificador)
        except Actor.DoesNotExist:
            raise Http404

        # Paso el actor al template
        context['actor'] = actor

        # Paso las peliculas donde actua el actor
        peliculas = actor.pelicula_set.all()
        context['peliculas'] = peliculas

        return context

class Detalle_Director(TemplateView):
    template_name = 'detalle-director.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        try:
            identificador = self.kwargs['id_director']

            # Busco el director por id
            director = Director.objects.get(id=identificador)
        except Director.DoesNotExist:
            raise Http404

        # Paso el director al template
        context['director'] = director

        # Paso las peliculas que dirigió el director
        peliculas = director.pelicula_set.all()
        context['peliculas'] = peliculas

        return context
    
# Función para cargar una pelicula   
def cargar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('peliculas')  # Redirige a la página de películas (ajusta esto según tu ruta)
    else:
        form = PeliculaForm()
    return render(request, 'cargar_pelicula.html', {'form': form})





from audioop import avg
from typing import Any, Dict
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView
from pagina_web.models import *
from django.shortcuts import render, redirect
from pagina_web.forms import *
from django.shortcuts import render
from django.db.models import Q
from django.db.models import F

# Create your views here.
class Inicio(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        peliculas = Pelicula.objects.all()
        context['peliculas'] = peliculas

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
        peliculas_mejor_puntaje = Pelicula.objects.order_by('-puntaje')[:18]
        context['peliculas_mejor_puntaje'] = peliculas_mejor_puntaje

        # Obtener las peliculas del carousel principal
        peliculas_carousel_principal = Pelicula.objects.filter(id__in=[21, 22, 23, 24, 25])
        context['peliculas_carousel_principal'] = peliculas_carousel_principal

        # Calcular las estrellas para cada película
        for pelicula in peliculas_mejor_puntaje:
            puntaje = pelicula.puntaje
            estrellas_llenas = range(puntaje)
            estrellas_vacias = range(5 - puntaje)

            pelicula.estrellas_llenas = estrellas_llenas
            pelicula.estrellas_vacias = estrellas_vacias

        return context

class Peliculas(TemplateView):
    template_name = 'peliculas.html'

    def get_queryset(self):
        queryset = Pelicula.objects.all()

        orden = self.request.GET.get('orden')
        categoria = self.request.GET.get('categoria')
        busqueda = self.request.GET.get('busqueda')
        
        if categoria:
            queryset = queryset.filter(categoria=categoria)

        if busqueda:
            queryset = queryset.filter(nombre__icontains=busqueda)

        if orden:
            queryset = queryset.order_by(orden)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        orden_actual = self.request.GET.get('orden')
        categoria_actual = self.request.GET.get('categoria')
        
        context['orden_actual'] = orden_actual
        context['categoria_actual'] = categoria_actual

        peliculas = self.get_queryset()
        context['peliculas'] = peliculas

        return context

class Actores(TemplateView):
    template_name = 'listado-actores.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        actores = Actor.objects.all()
        context['actores'] = actores

        return context
    
class Directores(TemplateView):
    template_name = 'directores.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        directores = Director.objects.all()
        context['directores'] = directores

        return context

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

        # Obtener las críticas asociadas a la película
        criticas = Critica.objects.filter(pelicula=pelicula, estado="APROBADO")
        context['criticas'] = criticas

        # Obtener la cantidad de estrellas para cada crítica
        estrellas_por_critica = []
        for critica in criticas:
            estrellas = range(critica.puntaje)
            estrellas_por_critica.append(list(estrellas))

        # Combinar las listas de criticas y estrellas_por_critica en una lista de tuplas
        criticas_con_estrellas = list(zip(criticas, estrellas_por_critica))
        context['criticas_con_estrellas'] = criticas_con_estrellas

        return context

    def post(self, request, *args, **kwargs):
        id_pelicula = self.kwargs['id']

        form = CriticaForm(request.POST)
        if form.is_valid():
            crítica = form.save(commit=False)
            crítica.pelicula_id = id_pelicula
            crítica.save()

            # Calculo el promedio de puntaje para la pelicula
            pelicula = Pelicula.objects.get(id=id_pelicula)
            criticas = Critica.objects.filter(pelicula=pelicula)

            # Calculate the total puntaje and the number of criticas
            total_puntaje = 0
            num_criticas = 0
            for critica in criticas:
                if critica.puntaje is not None:
                    total_puntaje += critica.puntaje
                    num_criticas += 1

            # Calculate the average puntaje
            if num_criticas > 0:
                average_puntaje = total_puntaje / num_criticas
            else:
                average_puntaje = 0

            pelicula.puntaje = average_puntaje
            pelicula.save()

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





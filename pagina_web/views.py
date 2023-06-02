from typing import Any, Dict
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from pagina_web.models import *
from django.shortcuts import render, redirect
from pagina_web.forms import *

# Create your views here.
class Inicio(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
      context = super().get_context_data(**kwargs)
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

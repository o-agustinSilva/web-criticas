from django.contrib import admin
from django.urls import path
from pagina_web.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view()),

    path('Peliculas/', Peliculas.as_view(), name='PeliculasView'),
    path('Actores/', Actores.as_view(), name='ActoresView'),
    path('Directores/', Directores.as_view(), name='DirectoresView'),

    path('Pelicula/<int:id>/', Detalle_Pelicula.as_view(), name='PeliculaView'),
    path('Actor/<int:id_actor>/', Detalle_Actor.as_view(), name='ActorView'),
    path('Director/<int:id_director>/', Detalle_Director.as_view(), name='DirectorView'),
    
    path('crear-pelicula/', cargar_pelicula, name='crear_pelicula'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

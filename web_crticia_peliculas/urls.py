from django.contrib import admin
from django.urls import path
from pagina_web.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio.as_view()),
    path('Pelicula/<int:id>/', Detalle_Pelicula.as_view(), name='id'),
    path('crear-pelicula/', cargar_pelicula, name='crear_pelicula'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

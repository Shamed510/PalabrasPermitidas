from django.urls import path
from . import views

urlpatterns = [
#Nombres de los funciones / mas los parametros que queramos enviar a sus respectivas funciones
    path('', views.home),
    path('agregarPalabra/', views.agregarPalabra),
    path('editarPalabra/<id>', views.editarPalabra),
    path('edicionPalabra/', views.edicionPalabra),
    path('borrarPalabra/<id>', views.borrarPalabra)
]

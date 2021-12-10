from django.urls import path

from .views import NuevoProveedor, ListadoProveedor

urlpatterns = [
    path('nuevoproveedor/', NuevoProveedor,name='nuevoproveedor'),
    path('listadoproveedor/',ListadoProveedor,name='listadoproveedor')
]
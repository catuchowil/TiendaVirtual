from django.urls import path

from .views import NuevoCliente, ListadoCliente
urlpatterns = [
    path('nuevocliente/', NuevoCliente, name='nuevocliente'),
    path('listadocliente/', ListadoCliente, name='listadocliente'),

    
]
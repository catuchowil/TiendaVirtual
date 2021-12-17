from django.urls import path

from .views import NuevoCliente, ListadoCliente, DetalleCliente
urlpatterns = [
    path('nuevocliente/', NuevoCliente.as_view(), name='nuevocliente'),
    path('listadocliente/', ListadoCliente.as_view(), name='listadocliente'),
    path('detallecliente/<int:pk>',DetalleCliente.as_view(),name='detallecliente')

    # Url de vistas basadas en función
    # path('nuevocliente/', NuevoCliente, name='nuevocliente'),
    #path('listadocliente/', ListadoCliente, name='listadocliente'),

    
]
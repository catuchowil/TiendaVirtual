from django.urls import path

from .views import NuevoCliente, ListadoCliente, DetalleCliente, BuscarCliente

urlpatterns = [
    path('nuevocliente/', NuevoCliente.as_view(), name='nuevocliente'),
    path('listadocliente/', ListadoCliente.as_view(), name='listadocliente'),
    path('detallecliente/<int:pk>',DetalleCliente.as_view(),name='detallecliente'),
    path('buscarcliente/',BuscarCliente.as_view(), name='buscarcliente')

    

    
]
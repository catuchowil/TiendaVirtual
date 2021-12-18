from django.urls import path

from .views import NuevoVendedor, ListadoVendedor,DetalleVendedor, BuscarVendedor

urlpatterns = [
    path('nuevovendedor/',NuevoVendedor.as_view(), name='nuevovendedor'),
    path('listadovendedor/',ListadoVendedor.as_view(),name='listadovendedor'),
    path('detallevendedor/<int:pk>',DetalleVendedor.as_view(),name='detallevendedor'),
    path('buscarvendedor/',BuscarVendedor.as_view(),name='buscarvendedor')

    # Urls de vistas basadas en función
    #path('nuevovendedor/',NuevoVendedor, name='nuevovendedor'),
    #path('listadovendedor/',ListadoVendedor,name='listadovendedor'),
]
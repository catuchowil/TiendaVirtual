from django.urls import path

from .views import NuevoVendedor, ListadoVendedor

urlpatterns = [
    path('nuevovendedor/',NuevoVendedor.as_view(), name='nuevovendedor'),
    path('listadovendedor/',ListadoVendedor.as_view(),name='listadovendedor'),

    # Urls de vistas basadas en función
    #path('nuevovendedor/',NuevoVendedor, name='nuevovendedor'),
    #path('listadovendedor/',ListadoVendedor,name='listadovendedor'),
]
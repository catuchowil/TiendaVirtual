from django.urls import path

from .views import NuevoVendedor, ListadoVendedor

urlpatterns = [
    path('nuevovendedor/',NuevoVendedor, name='nuevovendedor'),
    path('listadovendedor/',ListadoVendedor,name='listadovendedor')
]
from django.urls import path

from .views import NuevoProducto, ListadoProducto

urlpatterns = [
    path('nuevoproducto/',NuevoProducto,name='nuevoproducto'),
    path('listadoproducto/', ListadoProducto, name='listadoproducto')
]
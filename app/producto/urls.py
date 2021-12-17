from django.urls import path

from .views import NuevoProducto, ListadoProducto

urlpatterns = [
    # Url de vistas basadas en clase

    path('nuevoproducto/',NuevoProducto.as_view(),name='nuevoproducto'),
    path('listadoproducto/',ListadoProducto.as_view(), name='listadoproducto')

    # Url de vistas basadas en función
    #path('nuevoproducto/',NuevoProducto,name='nuevoproducto'),
    #path('listadoproducto/', ListadoProducto, name='listadoproducto'),
]
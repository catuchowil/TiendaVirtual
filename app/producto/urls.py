from django.urls import path

from .views import NuevoProducto, ListadoProducto, DetalleProducto, BuscarProducto

urlpatterns = [
    # Url de vistas basadas en clase

    path('nuevoproducto/',NuevoProducto.as_view(),name='nuevoproducto'),
    path('listadoproducto/',ListadoProducto.as_view(), name='listadoproducto'),
    path('detalleproducto/<int:pk>',DetalleProducto.as_view(),name='detalleproducto'),
    path('buscarproducto/',BuscarProducto.as_view(),name='buscarproducto')

    # Url de vistas basadas en función
    #path('nuevoproducto/',NuevoProducto,name='nuevoproducto'),
    #path('listadoproducto/', ListadoProducto, name='listadoproducto'),
]
from django.urls import path

from .views import NuevoProducto, ListadoProducto, DetalleProducto, BuscarProducto, EditarProducto, EliminarProducto

urlpatterns = [
    # Url de vistas basadas en clase

    path('nuevoproducto/',NuevoProducto.as_view(),name='nuevoproducto'),
    path('listadoproducto/',ListadoProducto.as_view(), name='listadoproducto'),
    path('detalleproducto/<int:pk>',DetalleProducto.as_view(),name='detalleproducto'),
    path('buscarproducto/',BuscarProducto.as_view(),name='buscarproducto'),
    path('editarproducto/<int:pk>',EditarProducto.as_view(),name='editarproducto'),
    path('eliminarproducto/<int:pk>',EliminarProducto.as_view(),name='eliminarproducto')

    # Url de vistas basadas en función
    #path('nuevoproducto/',NuevoProducto,name='nuevoproducto'),
    #path('listadoproducto/', ListadoProducto, name='listadoproducto'),
]
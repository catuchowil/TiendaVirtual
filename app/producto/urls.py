from django.urls import path

from .views import NuevoProducto

urlpatterns = [
    path('nuevoproducto/',NuevoProducto,name='nuevoproducto')
]
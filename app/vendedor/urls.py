from django.urls import path

from .views import NuevoVendedor

urlpatterns = [
    path('nuevovendedor/',NuevoVendedor, name='nuevovendedor')
]
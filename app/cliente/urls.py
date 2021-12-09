from django.urls import path

from .views import NuevoCliente

urlpatterns = [
    path('nuevocliente/', NuevoCliente, name='nuevocliente')
]
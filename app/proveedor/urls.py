from django.urls import path

from .views import NuevoProveedor

urlpatterns = [
    path('nuevoproveedor/', NuevoProveedor,name='nuevoproveedor')
]
from django.urls import path

from app.base.views import Home

#--Importamos las view de la aplicación base
from .views import Home

#--Generamos las urls de la aplicación base 

urlpatterns = [
    path('',Home, name='index')
]
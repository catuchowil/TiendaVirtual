from django.urls import path

from app.base.views import Home

#--Importamos las view de la aplicación base
from .views import Home, Acercade

#--Generamos las urls de la aplicación base 

urlpatterns = [
    
    # Url de vistas basadas en clase
    path('',Home.as_view(), name='index'),
    path('acercade/', Acercade.as_view(), name='acercade')


    #Url de vistas en funciones
    #path('',Home, name='index'),
    #path('acercade/', Acercade, name='acercade'),
   
]
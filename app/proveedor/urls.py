from django.urls import path

from .views import NuevoProveedor, ListadoProveedor

urlpatterns = [
    # Vistas Basadas en clase
    path('nuevoproveedor/', NuevoProveedor.as_view(),name='nuevoproveedor'),
    path('listadoproveedor/',ListadoProveedor.as_view(),name='listadoproveedor'),

    
    #Vistas Basadas en Función
    #path('nuevoproveedor/', NuevoProveedor,name='nuevoproveedor'),
    #path('listadoproveedor/',ListadoProveedor,name='listadoproveedor')
    
]
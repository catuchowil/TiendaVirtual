from django.urls import path

from .views import NuevoProveedor, ListadoProveedor,DetalleProveedor, BuscarProveedor

urlpatterns = [
    # Vistas Basadas en clase
    path('nuevoproveedor/', NuevoProveedor.as_view(),name='nuevoproveedor'),
    path('listadoproveedor/',ListadoProveedor.as_view(),name='listadoproveedor'),
    path('detalleproveedor/<int:pk>',DetalleProveedor.as_view(),name='detalleproveedor'),
    path('buscarproveedor/',BuscarProveedor.as_view(),name='buscarproveedor')

    
    #Vistas Basadas en Función
    #path('nuevoproveedor/', NuevoProveedor,name='nuevoproveedor'),
    #path('listadoproveedor/',ListadoProveedor,name='listadoproveedor')
    
]
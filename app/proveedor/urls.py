from django.urls import path

from .views import NuevoProveedor, ListadoProveedor,DetalleProveedor, BuscarProveedor, EditarProveedor, EliminarProveedor

urlpatterns = [
    # Vistas Basadas en clase
    path('nuevoproveedor/', NuevoProveedor.as_view(),name='nuevoproveedor'),
    path('listadoproveedor/',ListadoProveedor.as_view(),name='listadoproveedor'),
    path('detalleproveedor/<int:pk>',DetalleProveedor.as_view(),name='detalleproveedor'),
    path('buscarproveedor/',BuscarProveedor.as_view(),name='buscarproveedor'),
    path('editarproveedor/<int:pk>',EditarProveedor.as_view(),name='editarproveedor'),
    path('eliminarproveedor/<int:pk>',EliminarProveedor.as_view(),name='eliminarproveedor')


    
    #Vistas Basadas en Función
    #path('nuevoproveedor/', NuevoProveedor,name='nuevoproveedor'),
    #path('listadoproveedor/',ListadoProveedor,name='listadoproveedor')
    
]
from django.shortcuts import render
from .models import Producto

# Vista de Nuevo Producto.
def NuevoProducto(request):
    return render(request, 'producto/nuevo_producto.html')


# Vista Listado Cliente
def ListadoProducto(request):
    producto = Producto.objects.all() # Trae todos los registros de la tabla producto
    return render(request, 'producto/listado_producto.html',{'prod':producto})

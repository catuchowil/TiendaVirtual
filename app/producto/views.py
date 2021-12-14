from django.shortcuts import render, redirect
from .models import Producto

from .forms import ProductoForm

# Vista de Nuevo Producto.
def NuevoProducto(request):

    if request.method == 'POST':
        formulario_producto= ProductoForm(request.POST)
        if formulario_producto.is_valid():
            formulario_producto.save()
            return redirect('producto:listadoproducto')
    else:
        formulario_producto = ProductoForm()
    
    return render(request, 'producto/nuevo_producto.html',{'form':formulario_producto})

   


# Vista Listado Producto
def ListadoProducto(request):
    producto = Producto.objects.all() # Trae todos los registros de la tabla producto
    return render(request, 'producto/listado_producto.html',{'prod':producto})

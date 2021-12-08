from django.shortcuts import render

# Vista de Nuevo Producto.
def NuevoProducto(request):
    return render(request, 'producto/nuevo_producto.html')

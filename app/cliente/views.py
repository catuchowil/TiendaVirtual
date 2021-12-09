from django.shortcuts import render

# Vista de Nuevo Producto.
def NuevoCliente(request):
    return render(request, 'cliente/nuevo_cliente.html')

from django.shortcuts import render

from app.cliente.models import Cliente

# Vista de Nuevo Cliente.
def NuevoCliente(request):
    return render(request, 'cliente/nuevo_cliente.html')


# Vista Listado Cliente
def ListadoCliente(request):
    cliente = Cliente.objects.all() # Trae todos los registros de la tabla clientes
    return render(request, 'cliente/listado_cliente.html',{'cli':cliente})

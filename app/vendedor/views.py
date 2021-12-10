from django.shortcuts import render

from .models import Vendedor

# Vista de Nuevo Vendedor.
def NuevoVendedor(request):
    return render(request, 'vendedor/nuevo_vendedor.html')


# Vista Listado Cliente
def ListadoVendedor(request):
    vendedor = Vendedor.objects.all() # Trae todos los registros de la tabla vendedor
    return render(request, 'vendedor/listado_vendedor.html',{'vend':vendedor})


from django.shortcuts import render

from .models import Proveedor

# Vista de Nuevo Proveedor.
def NuevoProveedor(request):
    return render(request, 'proveedor/nuevo_proveedor.html')



# Vista Listado Proveedor
def ListadoProveedor(request):
    proveedor = Proveedor.objects.all() # Trae todos los registros de la tabla proveedor
    return render(request, 'proveedor/listado_proveedor.html',{'provee':proveedor})

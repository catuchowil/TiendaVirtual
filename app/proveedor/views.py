from django.shortcuts import render, redirect

from .models import Proveedor
from .forms import ProveedorForm

# Vista de Nuevo Proveedor.
def NuevoProveedor(request):

    if request.method == 'POST':
        formulario_proveedor= ProveedorForm(request.POST)
        if formulario_proveedor.is_valid():
            formulario_proveedor.save()
            return redirect('proveedor:listadoproveedor')
    else:
        formulario_proveedor = ProveedorForm()
    
    return render(request, 'proveedor/nuevo_proveedor.html',{'form':formulario_proveedor})

    



# Vista Listado Proveedor
def ListadoProveedor(request):
    proveedor = Proveedor.objects.all() # Trae todos los registros de la tabla proveedor
    return render(request, 'proveedor/listado_proveedor.html',{'provee':proveedor})

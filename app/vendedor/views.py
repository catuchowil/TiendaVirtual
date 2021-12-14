from django.shortcuts import render, redirect

from .models import Vendedor
from .forms import VendedorForm

# Vista de Nuevo Vendedor.
def NuevoVendedor(request):

    if request.method == 'POST':
        formulario_vendedor= VendedorForm(request.POST)
        if formulario_vendedor.is_valid():
            formulario_vendedor.save()
            return redirect('vendedor:listadovendedor')
    else:
        formulario_vendedor = VendedorForm()
    
    return render(request, 'vendedor/nuevo_vendedor.html',{'form':formulario_vendedor})

   


# Vista Listado Vendedor
def ListadoVendedor(request):
    vendedor = Vendedor.objects.all() # Trae todos los registros de la tabla vendedor
    return render(request, 'vendedor/listado_vendedor.html',{'vend':vendedor})


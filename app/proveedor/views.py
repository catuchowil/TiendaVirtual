from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from .models import Proveedor
from .forms import ProveedorForm

# Vistas Basadas en Clase
class NuevoProveedor(generic.CreateView):
    model = Proveedor
    template_name = 'proveedor/nuevo_proveedor.html'
    context_object_name = 'form'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor:listadoproveedor')


class ListadoProveedor(generic.ListView):
    model = Proveedor
    template_name = 'proveedor/listado_proveedor.html'
    context_object_name = 'provee'


class DetalleProveedor(generic.DetailView):
    model = Proveedor
    template_name = 'proveedor/detalle_proveedor.html'
    context_object_name = 'provee'


"""
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
"""

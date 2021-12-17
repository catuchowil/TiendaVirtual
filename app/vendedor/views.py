from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from .models import Vendedor
from .forms import VendedorForm


# Vistas Basadas en Clase
class NuevoVendedor(generic.CreateView):
    model = Vendedor
    template_name = 'vendedor/nuevo_vendedor.html'
    context_object_name = 'form'
    form_class = VendedorForm
    succes_url = reverse_lazy('vendedor:listadovendedor')


class ListadoVendedor(generic.ListView):
    model = Vendedor
    template_name = 'vendedor/listado_vendedor.html'
    context_object_name = 'vend'


class DetalleVendedor(generic.DetailView):
    model = Vendedor
    template_name = 'vendedor/detalle_vendedor.html'
    context_object_name = 'vend'



"""
VISTAS BASADAS EN FUNCION

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
"""


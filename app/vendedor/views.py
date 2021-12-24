from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Vendedor
from .forms import VendedorForm


# Vistas Basadas en Clase
class NuevoVendedor(LoginRequiredMixin,generic.CreateView):
    model = Vendedor
    template_name = 'vendedor/nuevo_vendedor.html'
    context_object_name = 'form'
    form_class = VendedorForm
    succes_url = reverse_lazy('vendedor:listadovendedor')
    login_url = 'base:login'


class ListadoVendedor(LoginRequiredMixin,generic.ListView):
    model = Vendedor
    template_name = 'vendedor/listado_vendedor.html'
    context_object_name = 'vend'
    login_url = 'base:login'


class DetalleVendedor(LoginRequiredMixin,generic.DetailView):
    model = Vendedor
    template_name = 'vendedor/detalle_vendedor.html'
    context_object_name = 'vend'
    login_url = 'base:login'


class BuscarVendedor(LoginRequiredMixin,generic.ListView):
    template_name = 'vendedor/buscar_vendedor.html'
    context_object_name = 'vend'
    login_url = 'base:login'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword")
        if not palabra_clave:
            palabra_clave = "None"
        return Vendedor.objects.filter(apellido_vendedor__icontains=palabra_clave)



class EditarVendedor(LoginRequiredMixin,generic.UpdateView):
    model = Vendedor
    template_name = 'vendedor/editar_vendedor.html'
    context_object_name = 'obj'
    form_class = VendedorForm
    success_url = reverse_lazy('vendedor:listadovendedor')
    login_url = 'base:login'



class EliminarVendedor(LoginRequiredMixin,generic.DeleteView):
    model = Vendedor
    template_name = 'vendedor/eliminar_vendedor.html'
    success_url = reverse_lazy('vendedor:listadovendedor')
    login_url = 'base:login'



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


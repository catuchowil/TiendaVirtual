from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Proveedor
from .forms import ProveedorForm

# Vistas Basadas en Clase
class NuevoProveedor(LoginRequiredMixin,generic.CreateView):
    model = Proveedor
    template_name = 'proveedor/nuevo_proveedor.html'
    context_object_name = 'form'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor:listadoproveedor')
    login_url = 'base:login'


class ListadoProveedor(LoginRequiredMixin,generic.ListView):
    model = Proveedor
    template_name = 'proveedor/listado_proveedor.html'
    context_object_name = 'provee'
    login_url = 'base:login'


class DetalleProveedor(LoginRequiredMixin,generic.DetailView):
    model = Proveedor
    template_name = 'proveedor/detalle_proveedor.html'
    context_object_name = 'provee'
    login_url = 'base:login'


class BuscarProveedor(LoginRequiredMixin,generic.ListView):
    template_name = 'proveedor/buscar_proveedor.html'
    context_object_name = 'provee'
    login_url = 'base:login'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword")
        if not palabra_clave:
            palabra_clave = "None"
        return Proveedor.objects.filter(nombre_proveedor__icontains=palabra_clave)


class EditarProveedor(LoginRequiredMixin,generic.UpdateView):
    model = Proveedor
    template_name = 'proveedor/editar_proveedor.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor:listadoproveedor')
    login_url = 'base:login'



class EliminarProveedor(LoginRequiredMixin,generic.DeleteView):
    model = Proveedor
    template_name = 'proveedor/eliminar_proveedor.html'
    success_url = reverse_lazy('proveedor:listadoproveedor')
    login_url = 'base:login'


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

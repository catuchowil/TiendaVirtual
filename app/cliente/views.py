from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from app.cliente.models import Cliente
from .forms import ClienteForm

# Vistas Basadas en Clase

class NuevoCliente(generic.CreateView):
    model = Cliente
    template_name = 'cliente/nuevo_cliente.html'
    context_object_name = 'form'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:listadocliente')


class ListadoCliente(generic.ListView):
    model = Cliente
    template_name = 'cliente/listado_cliente.html'
    context_object_name = 'cli'


class DetalleCliente(generic.DetailView):
    model = Cliente
    template_name = 'cliente/detalle_cliente.html'
    context_object_name = 'cli'


class BuscarCliente(generic.ListView):
    template_name = 'cliente/buscar_cliente.html'
    context_object_name = 'cli'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword")
        if not palabra_clave:
            palabra_clave = "None"
        return Cliente.objects.filter(apellido_cliente__icontains=palabra_clave)



class EditarCliente(generic.UpdateView):
    model = Cliente
    template_name = 'cliente/editar_cliente.html'
    context_object_name = 'obj'
    form_class = ClienteForm
    success_url = reverse_lazy('cliente:listadocliente')



class EliminarCliente(generic.DeleteView):
    model = Cliente
    template_name = 'cliente/eliminar_cliente.html'
    
  
    success_url = reverse_lazy('cliente:listadocliente')



"""
VISTAS BASADAS EN FUNCIONES

# Vista de Nuevo Cliente.
def NuevoCliente(request):

    if request.method == 'POST':
        formulario_cliente= ClienteForm(request.POST)
        if formulario_cliente.is_valid():
            formulario_cliente.save()
            return redirect('cliente:listadocliente')
    else:
        formulario_cliente = ClienteForm()
    
    return render(request, 'cliente/nuevo_cliente.html',{'form':formulario_cliente})

  


# Vista Listado Cliente
def ListadoCliente(request):
    cliente = Cliente.objects.all() # Trae todos los registros de la tabla clientes
    return render(request, 'cliente/listado_cliente.html',{'cli':cliente})
"""



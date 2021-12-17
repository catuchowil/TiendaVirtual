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



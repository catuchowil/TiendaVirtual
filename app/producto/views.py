from django.shortcuts import render, redirect


from django.urls import reverse_lazy
from django.views import generic


from .models import Producto
from .forms import ProductoForm

# Vistas Basadas en Clase

class NuevoProducto(generic.CreateView):
    model = Producto
    template_name = 'producto/nuevo_producto.html'
    form_class = ProductoForm
    contex_object_name = 'form'
    success_url = reverse_lazy('producto:listadoproducto')


class ListadoProducto(generic.ListView):
    model = Producto
    template_name = 'producto/listado_producto.html'
    context_object_name = 'produ'


class DetalleProducto(generic.DetailView):
    model = Producto
    template_name = 'producto/detalle_producto.html'
    context_object_name = 'produ'


class BuscarProducto(generic.ListView):
    template_name = 'producto/buscar_producto.html'
    context_object_name = 'produ'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword")
        if not palabra_clave:
            palabra_clave = "None"
        return Producto.objects.filter(nombre_producto__icontains=palabra_clave)


   

"""
#Vistas Basadas en Función

# Vista de Nuevo Producto.
def NuevoProducto(request):

    if request.method == 'POST':
        formulario_producto= ProductoForm(request.POST)
        if formulario_producto.is_valid():
            formulario_producto.save()
            return redirect('producto:listadoproducto')
    else:
        formulario_producto = ProductoForm()
    
    return render(request, 'producto/nuevo_producto.html',{'form':formulario_producto})

   


# Vista Listado Producto
def ListadoProducto(request):
    producto = Producto.objects.all() # Trae todos los registros de la tabla producto
    return render(request, 'producto/listado_producto.html',{'produ':producto})
"""

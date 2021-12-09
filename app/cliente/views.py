from django.shortcuts import render

# Vista de Nuevo Cliente.
def NuevoCliente(request):
    return render(request, 'cliente/nuevo_cliente.html')

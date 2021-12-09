from django.shortcuts import render

# Vista de Nuevo Vendedor.
def NuevoVendedor(request):
    return render(request, 'vendedor/nuevo_vendedor.html')

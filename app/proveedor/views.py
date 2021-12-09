from django.shortcuts import render

# Vista de Nuevo Proveedor.
def NuevoProveedor(request):
    return render(request, 'proveedor/nuevo_proveedor.html')

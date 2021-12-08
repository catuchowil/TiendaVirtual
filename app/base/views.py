from django.shortcuts import render

# Vista de Inicio.
def Home(request):
    return render(request, 'base/home.html')


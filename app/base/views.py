from django.shortcuts import render
from django.views import generic

"""

Vistas Basadas en Función

# Vista de Inicio.
def Home(request):
    return render(request, 'base/home.html')


# Vista de Acercade
def Acercade(request):
    return render(request, 'base/acercade.html')
"""


# Vistas basadas en clase

class Home(generic.TemplateView):
    template_name = 'base/home.html'


class Acercade(generic.TemplateView):
    template_name = 'base/acercade.html'
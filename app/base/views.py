from django.shortcuts import render
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

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

class Home(LoginRequiredMixin,generic.TemplateView):
    template_name = 'base/home.html'
    login_url = 'base:login'


class Acercade(LoginRequiredMixin,generic.TemplateView):
    template_name = 'base/acercade.html'
    login_url = 'base:login'
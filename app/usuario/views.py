from django.shortcuts import render

from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.urls import reverse_lazy

from .forms import RegistroForm

# Create your views here.
class RegistroUsuario(LoginRequiredMixin,generic.CreateView):
    model = User
    template_name = 'usuario/nuevo_usuario.html'
    context_object_name = 'form'
    form_class = RegistroForm
    success_url = reverse_lazy('base:index')
    login_url = 'base:login'



class EditarUsuario(LoginRequiredMixin,generic.UpdateView):
    model = User
    template_name = 'usuario/editar_usuario.html'
    context_object_name = 'form'
    form_class = RegistroForm
    success_url = reverse_lazy('base:index')
    login_url = 'base:login'
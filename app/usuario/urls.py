from django.urls import path
from .views import RegistroUsuario



urlpatterns = [

     path('nuevousuario/', RegistroUsuario.as_view(), name='nuevousuario'),

]
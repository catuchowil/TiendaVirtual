from django.urls import path
from .views import RegistroUsuario, EditarUsuario



urlpatterns = [

     path('nuevousuario/', RegistroUsuario.as_view(), name='nuevousuario'),
     path('editarusuario/<int:pk>',EditarUsuario.as_view(),name='editarusuario'),

]
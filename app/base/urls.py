from django.urls import path

from app.base.views import Home

#--Importamos las view de la aplicación base
from .views import Home, Acercade

from django.contrib.auth import views as auth_views

#--Generamos las urls de la aplicación base 

urlpatterns = [
    
    # Url de vistas basadas en clase
    path('',Home.as_view(), name='index'),
    path('acercade/', Acercade.as_view(), name='acercade'),

    path('login/',auth_views.LoginView.as_view(template_name='base/login.html'),name='login'),
	path('logout/',auth_views.LogoutView.as_view(template_name='base/login.html'),name='logout'),


    #Url de vistas en funciones
    #path('',Home, name='index'),
    #path('acercade/', Acercade, name='acercade'),
   
]
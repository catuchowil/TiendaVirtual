"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('app.base.urls','base'),namespace='base')),
    path('producto/',include(('app.producto.urls','producto'),namespace='producto')),
    path('cliente/',include(('app.cliente.urls','cliente'),namespace='cliente')),
    path('vendedor/',include(('app.vendedor.urls','vendedor'),namespace='vendedor')),
    path('proveedor/',include(('app.proveedor.urls','proveedor'),namespace='proveedor')),
    path('usuario/',include(('app.usuario.urls','usuario'),namespace='usuario'))
]

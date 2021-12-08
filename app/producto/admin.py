from django.contrib import admin

from .models import Categoria, Nacionalidad, Marca, Producto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Nacionalidad)
admin.site.register(Marca)
admin.site.register(Producto) 

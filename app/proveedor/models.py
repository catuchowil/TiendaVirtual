from django.db import models

from app.cliente.models import Pais
# Create your models here.
class Proveedor(models.Model):
    codigo_proveedor = models.CharField(max_length=50, verbose_name='Código')
    nombre_proveedor = models.CharField(max_length=50, verbose_name='Nombre')
    domicilio_proveedor = models.CharField(max_length=150, verbose_name='Domicilio')
    telfijo_proveedor = models.CharField(max_length=10, verbose_name='Teléfono',null=True, blank=True)
    movil_proveedor = models.CharField(max_length=10, verbose_name='Celular',null=True, blank=True)
    email_proveedor = models.EmailField(verbose_name='Correo Electrónico',null=True, blank=True)
    zipcode_proveedor = models.CharField(max_length=10, verbose_name='Código Postal') 
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE,verbose_name='Pais')
   
    

    def __str__(self):
        return 'Nombre Proveedor: {}'.format(self.nombre_proveedor)
    
   
    class Meta:
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre_proveedor'] 
from django.db import models

# Create your models here.
SUCURSAL =(
    ('0', 'Seleccionar Sucursal'),
    ('1', 'Casa Central'),
    ('2', 'Sucursal Centro 1'),
    ('3', 'Sucursal Centro 2'),
    ('4', 'Sucursal Oeste 1'),
    ('5', 'Sucursal Sur 1'),


    )


class Vendedor(models.Model):
    nombre_vendedor = models.CharField(max_length=50, verbose_name='Nombre')
    apellido_vendedor = models.CharField(max_length=50, verbose_name='Apellido')
    dni_vendedor = models.CharField(max_length=10, verbose_name='DNI') 
    domicilio_vendedor = models.CharField(max_length=150, verbose_name='Domicilio')
    codigo_vendedor = models.CharField(max_length=10, verbose_name='Código',null=True, blank=True)
    sucursal = models.CharField(max_length=1,verbose_name='Sucursal',choices=SUCURSAL, default='0')
    
   
    

    def __str__(self):
        return 'Apellido y Nombre: {}, {}'.format(self.apellido_vendedor,self.nombre_vendedor)
    
   
    class Meta:
        verbose_name_plural = 'Vendedores'
        ordering = ['apellido_vendedor'] 


from django.db import models

# Create your models here.
class Pais(models.Model):

    pais = models.CharField(max_length=150, verbose_name='Pais',unique=True,
                blank=False, null=False)
    

    def __str__(self):
        return '{}'.format(self.pais)
    
        
    class Meta:
        verbose_name_plural = "Paises"
        ordering = ['pais']




class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=50, verbose_name='Nombre')
    apellido_cliente = models.CharField(max_length=50, verbose_name='Apellido')
    dni_cliente = models.CharField(max_length=10, verbose_name='DNI') 
    domicilio_cliente = models.CharField(max_length=150, verbose_name='Domicilio')
    telfijo_cliente = models.CharField(max_length=10, verbose_name='Teléfono',null=True, blank=True)
    movil_cliente = models.CharField(max_length=10, verbose_name='Celular',null=True, blank=True)
    email_cliente = models.EmailField(verbose_name='Correo Electrónico',null=True, blank=True)
    zipcode_cliente = models.CharField(max_length=10, verbose_name='Código Postal') 
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE,verbose_name='Pais')
   
    

    def __str__(self):
        return 'Apellido y Nombre: {}, {}'.format(self.apellido_cliente,self.nombre_cliente)
    
   
    class Meta:
        verbose_name_plural = 'Clientes'
        ordering = ['apellido_cliente'] 
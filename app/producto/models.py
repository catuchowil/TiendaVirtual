from django.db import models

# Create your models here.
class Categoria(models.Model):

    nombre = models.CharField(max_length=150, verbose_name='Nombre de la Categoría',unique=True,
                blank=False, null=False)
    

    def __str__(self):
        return '{}'.format(self.nombre)
    
    
    class Meta:
        verbose_name_plural = "Categorias"
        ordering = ['nombre']


class Nacionalidad(models.Model):

    nacionalidad = models.CharField(max_length=150, verbose_name='Nacionalidad Producto',unique=True,
                blank=False, null=False)
    

    def __str__(self):
        return '{}'.format(self.nacionalidad)

    
    class Meta:
        verbose_name_plural = "Nacionalidades"
        ordering = ['nacionalidad']



class Marca(models.Model):

    marca = models.CharField(max_length=150, verbose_name='Marca Producto',unique=True,
                blank=False, null=False)
    

    def __str__(self):
        return '{}'.format(self.marca)

    
    class Meta:
        verbose_name_plural = "Marcas"
        ordering = ['marca']




class Producto(models.Model):
    codigo_producto = models.CharField(max_length=10, verbose_name='Código Producto',unique=True)
    nombre_producto = models.CharField(max_length=150, verbose_name='Nombre Producto', unique=True,)
    descripcion_producto = models.TextField(blank=True, null=True, verbose_name='Características') 
    precio_unitario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,
                    verbose_name='Precio Unitario')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name='Categoria Producto')
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE,verbose_name='Nacionalidad Producto')
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE,verbose_name='Marca Producto')
   
    

    def __str__(self):
        return '{}{}{}'.format(self.codigo_producto,self.nombre_producto,self.id_categoria)
    

    class Meta:
        verbose_name_plural = 'Productos'
        ordering = ['nombre_producto'] 
from django.db import models
from core.models import ClaseModelo

# Create your models here.
class Categorias(ClaseModelo):
    nombre = models.CharField(max_length=100, help_text='Nombre categoría', unique=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['nombre']
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Categorias, self).save()

    def __str__(self):
        return self.nombre

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100, help_text='Nombre subcategoría')

    def __str__(self):
        return '{}: {}'.format(self.categoria.nombre, self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name = 'subcategoría'
        verbose_name_plural = 'subcategorías'
        ordering = ['nombre']
        unique_together = ('categoria', 'nombre')

class Marcas(ClaseModelo):
    nombre = models.CharField(max_length=150, help_text='Nombre de la marca', unique=True)

    def __str__(self):
        return self.nombre
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Marcas, self).save()
    
    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['nombre']

class UnidadMedida(ClaseModelo):
    nombre = models.CharField(max_length=150, help_text='Nombre de la UM', unique=True)

    def __str__(self):
        return self.nombre
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(UnidadMedida, self).save()
    
    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'
        ordering = ['nombre']

class Productos(ClaseModelo):
    codigo = models.CharField(max_length=20, unique=True)
    codigo_barra = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
    ultima_compra = models.DateField(null=True, blank=True)

    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre)
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Productos,self).save()
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['codigo']
        unique_together = ('codigo','codigo_barra')

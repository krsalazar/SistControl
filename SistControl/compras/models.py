from django.db import models
from core.models import ClaseModelo
from catalogos.models import Productos

# Create your models here.
class Proveedor(ClaseModelo):
    nombre = models.CharField(max_length=150, verbose_name='Nombre Proveedor', unique=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    contacto = models.CharField(max_length=75, verbose_name='Persona de contacto', null=True, blank=True)
    telefono = models.CharField(max_length=12, verbose_name='Teléfono', null=True, blank=True)
    email = models.EmailField(max_length=254, verbose_name='Correo electrónico', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Proveedor, self).save()
    
    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        ordering = ['nombre']

class ComprasEncabezado(ClaseModelo):
    fecha_compra = models.DateField(null=True, blank=True)
    observaciones = models.TextField(blank=True, null=True)
    no_fact = models.CharField(max_length=100)
    fecha_factura = models.DateField()
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    total = models.FloatField(default=0)


    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.observaciones
    
    def save(self):
        self.observaciones = self.observaciones.upper()
        self.iva = ((self.sub_total - self.descuento) / 1.12)*0.12
        self.total = self.sub_total - self.descuento
        super(ComprasEncabezado, self).save()
    
    class Meta:
        verbose_name = 'Encabezado de compra'
        verbose_name_plural = 'Encabezados de compras'

class ComprasDetalle(ClaseModelo):
    compra = models.ForeignKey(ComprasEncabezado, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio_comp = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return self.producto
    
    def save(self):
        self.sub_total = float(self.cantidad) * float(self.precio_comp)
        self.iva = ((self.sub_total-self.descuento)/1.12)*0.12
        self.total = self.sub_total-self.descuento
        super(ComprasDetalle, self).save()
       
    class Meta:
        verbose_name = 'Detalle de compra'

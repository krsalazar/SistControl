from django.contrib import admin
from .models import *

# Register your models here.
class AdmonProveedor(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdmonEncabezado(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdmonDetalle(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Proveedor, AdmonProveedor)
admin.site.register(ComprasEncabezado, AdmonEncabezado)
admin.site.register(ComprasDetalle, AdmonDetalle)
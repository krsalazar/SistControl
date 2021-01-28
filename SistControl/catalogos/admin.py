from django.contrib import admin
from .models import *
# Register your models here.

class AdmonCategorias(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdmonSubCategoria(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdmonMarcas(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdmonUm(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdmonProductos(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categorias, AdmonCategorias)
admin.site.register(SubCategoria, AdmonSubCategoria)
admin.site.register(Marcas, AdmonMarcas)
admin.site.register(UnidadMedida, AdmonUm)
admin.site.register(Productos, AdmonProductos)
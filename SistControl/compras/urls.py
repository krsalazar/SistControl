from django.urls import path
from .views import *

urlpatterns = [
    path('proveedores/', Proveedores.as_view(), name='lista_proveedores'),
    path('proveedores/nuevo/', NuevoProveedor.as_view(), name='nuevo_proveedor'),
    path('proveedores/editar/<int:pk>', EditarProveedor.as_view(), name='editar_proveedor'),
    path('proveedores/inactiv/<int:id>', inactivar_proveedor, name='inactivar_proveedor'),

    path('compras/', Compras.as_view(), name='lista_compras'),
    path('compras/nuevo', compraview, name='compras_new'),
    path('compras/editar/<int:compra_id>', compraview, name = 'editar_compras'),

]

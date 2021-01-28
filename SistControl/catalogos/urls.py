from django.urls import path
from .views import *

urlpatterns = [
    path('categorias/', Categoria.as_view(), name='lista_categoria'),
    path('categorias/nuevo/', NuevoCategoria.as_view(), name='nueva_categoria'),
    path('categorias/editar/<int:pk>', EditarCategoria.as_view(), name='editar_categoria'),
    path('categorias/borrar/<int:pk>', BorrarCategoria.as_view(), name='borrar_categoria'),

    path('subcategorias/', SubCategorias.as_view(), name='lista_subcategoria'),
    path('subcategorias/nuevo/', NuevoSubCategoria.as_view(), name='nueva_subcategoria'),
    path('subcategorias/editar/<int:pk>', EditarSubCategoria.as_view(), name='editar_subcategoria'),
    path('subcategorias/borrar/<int:pk>', BorrarSubCategoria.as_view(), name='borrar_subcategoria'),

    path('marcas/', Marca.as_view(), name='lista_marcas'),
    path('marcas/nuevo/', NuevaMarca.as_view(), name='nueva_marca'),
    path('marcas/editar/<int:pk>', EditarMarca.as_view(), name='editar_marca'),
    path('marcas/inactiv/<int:id>', inactivar, name='inactivar_marca'),

    path('ums/', UMVista.as_view(), name='lista_um'),
    path('ums/nuevo/', NuevaUM.as_view(), name='nueva_um'),
    path('ums/editar/<int:pk>', EditarUMS.as_view(), name='editar_um'),
    path('ums/inactiv/<int:id>', inactivarUM, name='inactivar_um'),

    path('productos/',Producto.as_view(), name="lista_producto"),
    path('productos/nuevo',NuevoProducto.as_view(), name="nuevo_producto"),
    path('productos/editar/<int:pk>',EditarProducto.as_view(), name="editar_producto"),
    path('productos/inactiv/<int:id>',inactivar_producto, name="inactivar_producto"),

]

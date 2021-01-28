from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from core.views import SinAcceso
from .models import *
from .forms import *

# Create your views here.
class Categoria(SinAcceso, generic.ListView):
    permission_required = 'catalogos.view_categorias'    
    model = Categorias
    template_name = 'catalogos/lista_categoria.html'
    context_object_name = 'categorias'
    

class NuevoCategoria(SuccessMessageMixin, SinAcceso, generic.CreateView):
    permission_required = 'catalogos.add_categorias'
    model = Categorias
    template_name = 'catalogos/form_categoria.html'
    context_object_name = 'categorias'
    form_class = FormCategoria
    success_url = reverse_lazy('categorias:lista_categoria')
    success_message = 'Se ha creado una nueva categoría'

#Agregamos el Id del usuario que crea la categoría
    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class EditarCategoria(SuccessMessageMixin, SinAcceso, generic.UpdateView):
    permission_required = 'catalogos.change_categorias'
    model = Categorias
    template_name = 'catalogos/form_categoria.html'
    context_object_name = 'categorias'
    form_class = FormCategoria
    success_url = reverse_lazy('categorias:lista_categoria')
    success_message = 'Se ha modificado categoría'


#Agregamos el Id del usuario que crea la categoría
    def form_valid(self, form):
        form.instance.modificador = self.request.user.id
        return super().form_valid(form)

class BorrarCategoria(LoginRequiredMixin, generic.DeleteView):
    model = Categorias
    template_name = 'catalogos/delete.html'
    context_object_name = 'categorias'
    success_url = reverse_lazy('categorias:lista_categoria')
    login_url = 'core:login'

class SubCategorias(SinAcceso, generic.ListView):
    permission_required = 'catalogos.view_subcategoria'
    model = SubCategoria
    template_name = 'catalogos/lista_subcategoria.html'
    context_object_name = 'subcategorias'

class NuevoSubCategoria(SuccessMessageMixin, SinAcceso, generic.CreateView):
    permission_required = 'catalogos.add_subcategoria'
    model = SubCategoria
    template_name = 'catalogos/form_subcategoria.html'
    context_object_name = 'subcategorias'
    form_class = FormSubCategoria
    success_url = reverse_lazy('categorias:lista_subcategoria')
    success_message = 'Se ha creado una nueva subcategoría'


#Agregamos el Id del usuario que crea la categoría
    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class EditarSubCategoria(SuccessMessageMixin, SinAcceso, generic.UpdateView):
    permission_required = 'catalogos.change_categorias'
    model = SubCategoria
    template_name = 'catalogos/form_subcategoria.html'
    context_object_name = 'categorias'
    form_class = FormSubCategoria
    success_url = reverse_lazy('categorias:lista_subcategoria')
    success_message = 'Se ha modificado la categoría'


#Agregamos el Id del usuario que crea la categoría
    def form_valid(self, form):
        form.instance.modificador = self.request.user.id
        return super().form_valid(form)

class BorrarSubCategoria(LoginRequiredMixin, generic.DeleteView):
    model = SubCategoria
    template_name = 'catalogos/delete.html'
    context_object_name = 'categorias'
    success_url = reverse_lazy('categorias:lista_subcategoria')
    login_url = 'core:login'

class Marca(SinAcceso, generic.ListView):
    permission_required = 'catalogos.view_marcas'
    model = Marcas
    template_name = 'catalogos/lista_marca.html'
    context_object_name = 'marcas'

class NuevaMarca(SuccessMessageMixin, SinAcceso, generic.CreateView):
    permission_required = 'catalogos.add_marcas'
    model = Marcas
    template_name = 'catalogos/form_marca.html'
    context_object_name = 'marcas'
    form_class = FormMarca    
    success_url = reverse_lazy('categorias:lista_marcas')
    success_message = 'Se ha creado una nueva marca'


    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class EditarMarca(SuccessMessageMixin, SinAcceso, generic.UpdateView):
    permission_required = 'catalogos.change_marcas'
    model = Marcas
    template_name = 'catalogos/form_marca.html'
    context_object_name = 'marcas'
    form_class = FormMarca    
    success_url = reverse_lazy('categorias:lista_marcas')
    success_message = 'Se ha modificado la marca'


    def form_valid(self, form):
        form.instance.modificador = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('catalogos.change_marcas', login_url='core:denegado')
def inactivar(request, id):
    marca = Marcas.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'catalogos/delete.html'

    if not marca:
        return redirect('categorias:lista_marcas')
    
    if request.method=='GET':
        contexto={'categorias':marca}
    
    if request.method=='POST':
        marca.estado = False
        marca.save()
        messages.success(request, 'Se ha inactivado la marca')
        return redirect('categorias:lista_marcas')
    
    return render(request,template_name, contexto)

class UMVista(SinAcceso, generic.ListView):
    permission_required = 'catalogos.view_unidadmedida'
    model = UnidadMedida
    template_name = 'catalogos/lista_um.html'
    context_object_name = 'UMS'

class NuevaUM(SuccessMessageMixin, SinAcceso, generic.CreateView):
    permission_required = 'catalogos.add_unidadmedida'
    model = UnidadMedida
    template_name = 'catalogos/form_um.html'
    context_object_name = 'UMS'
    form_class = FormUm  
    success_url = reverse_lazy('categorias:lista_um')
    success_message = 'Se ha creado una nueva unidad de medida'


    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class EditarUMS(SuccessMessageMixin, SinAcceso, generic.UpdateView):
    permission_required = 'catalogos.change_unidadmedida'
    model = UnidadMedida
    template_name = 'catalogos/form_um.html'
    context_object_name = 'UMS'
    form_class = FormUm   
    success_url = reverse_lazy('categorias:lista_um')
    success_message = 'Se ha modificado la unidad de medida'


    def form_valid(self, form):
        form.instance.modificador = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('catalogos.change_unidadmedida', login_url='core:denegado')
def inactivarUM(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'catalogos/delete.html'

    if not um:
        return redirect('categorias:lista_um')
    
    if request.method=='GET':
        contexto={'categorias':um}
    
    if request.method=='POST':
        um.estado = False
        um.save()
        messages.success(request, 'Se ha inactivado la unidad de medida')
        return redirect('categorias:lista_um')
    
    return render(request,template_name, contexto)

class Producto(SinAcceso, generic.ListView):
    permission_required = 'catalogos.view_productos'
    model = Productos
    template_name = "catalogos/lista_producto.html"
    context_object_name = "productos"


class NuevoProducto(SuccessMessageMixin, SinAcceso, generic.CreateView):
    permission_required = 'catalogos.add_productos'
    model=Productos
    template_name="catalogos/form_productos.html"
    context_object_name = 'productos'
    form_class=FormProductos
    success_url = reverse_lazy('categorias:lista_producto')
    success_message = 'Se ha creado un nuevo producto'


    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)
    

class EditarProducto(SuccessMessageMixin, SinAcceso, generic.UpdateView):
    permission_required = 'catalogos.change_productos'
    model=Productos
    template_name="catalogos/form_productos.html"
    context_object_name = 'productos'
    form_class=FormProductos
    success_url = reverse_lazy('categorias:lista_producto')
    success_message = 'Se ha modificado el producto'


    def form_valid(self, form):
        form.instance.modificador = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('catalogos.change_productos', login_url='core:denegado')
def inactivar_producto(request, id):
    prod = Productos.objects.filter(pk=id).first()
    contexto={}
    template_name="catalogos/delete.html"

    if not prod:
        return redirect("categorias:lista_producto")
    
    if request.method=='GET':
        contexto={'categorias':prod}
    
    if request.method=='POST':
        prod.estado=False
        prod.save()
        messages.success(request, 'Se ha inactivado el producto')
        return redirect("categorias:lista_producto")

    return render(request,template_name,contexto)
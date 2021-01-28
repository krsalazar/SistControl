from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.models import Sum
from core.views import SinAcceso
from catalogos.models import Productos
from .forms import *
from .models import *
import json
import datetime

# Create your views here.
class Proveedores(SinAcceso, generic.ListView):
    permission_required = 'compras.view_proveedores' 
    model = Proveedor
    template_name = 'compras/lista_proveedores.html'
    context_object_name = 'proveedores'

class NuevoProveedor(SuccessMessageMixin ,SinAcceso, generic.CreateView):
    permission_required = 'compras.add_proveedores'
    model = Proveedor
    template_name = 'compras/form_proveedores.html'
    context_object_name = 'proveedores'
    form_class = FormProveedor
    success_url = reverse_lazy('compras:lista_proveedores')
    success_message = 'Se ha creado un nuevo proveedor'

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class EditarProveedor(SuccessMessageMixin ,SinAcceso, generic.UpdateView):
    permission_required = 'compras.change_proveedores'
    model=Proveedor
    template_name="compras/form_proveedores.html"
    context_object_name = 'proveedores'
    form_class=FormProveedor
    success_url = reverse_lazy('compras:lista_proveedores')
    success_message = 'Se ha actualizado el proveedor'

    def form_valid(self, form):
        form.instance.modificador = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
@permission_required('copras.change_proveedores', login_url='core:denegado')
def inactivar_proveedor(request, id):
    prov = Proveedor.objects.filter(pk=id).first()
    contexto={}
    template_name="compras/delete.html"

    if not prov:
        return HttpResponse('No existe el proveedor ' + str(id))

    if request.method == 'GET':
        contexto ={'proveedores':prov}

    if request.method == 'POST':
        prov.estado = False
        prov.save()
        messages.success(request, 'Se ha inactivado el proveedor')
        return redirect("compras:lista_proveedores")

    return render(request,template_name,contexto)

class Compras(SinAcceso, generic.ListView):
    permission_required = 'compras.view_comprasencabezado' 
    model = ComprasEncabezado
    template_name = 'compras/lista_compras.html'
    context_object_name = 'comp'

@login_required(login_url='/login/')
@permission_required('copras.change_comprasencabezado', login_url='core:denegado')
def compraview(request, compra_id=None):
    template_name = 'compras/compras.html'
    prod = Productos.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    if request.method == 'GET':
        form_compras = FormCompraEnc()
        enc = ComprasEncabezado.objects.filter(pk=compra_id).first()
        #Si existe el encabezado...
        if enc:
            detalle = ComprasDetalle.objects.filter(compra=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra':fecha_compra,
                'proveedor':enc.proveedor,
                'fecha_factura':fecha_factura,
                'no_fact':enc.no_fact,
                'observaciones':enc.observaciones,
                'sub_total':enc.sub_total,
                'descuento':enc.descuento,
                'iva':enc.iva,
                'total':enc.total
            }
            #Inicializa el formulario con los campos que le asignamos a la variable e
            form_compras = FormCompraEnc(e)
        else:
            detalle = None
        
        contexto = {'productos':prod, 'encabezado':enc, 'detalle':detalle, 'form_enc':form_compras}

    if request.method == 'POST':
#Si es un POST, capturamos los datos que se encuentran en el form
    #Iniciamos con los datos del encabezado
        fecha_compra = request.POST.get('fecha_compra')
        proveedor = request.POST.get('proveedor')
        fecha_factura = request.POST.get('fecha_factura')
        no_fact = request.POST.get('no_fact')
        observaciones = request.POST.get('observaciones')
        sub_total = 0
        descuento = 0
        iva = 0
        total = 0

        if not compra_id:
            prov = Proveedor.objects.get(pk=proveedor)
            #Usando los campos definidos en el modelo
            enc = ComprasEncabezado(
                fecha_compra = fecha_compra,
                observaciones = observaciones,
                no_fact = no_fact,
                fecha_factura = fecha_factura,
                proveedor = prov,
                creador = request.user
            )
            if enc:
                enc.save()
                compra_id = enc.id
        else:
            enc = ComprasEncabezado.objects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_compra = fecha_compra
                enc.fecha_factura = fecha_factura
                enc.observaciones = observaciones
                enc.no_fact = no_fact
                enc.save()
        
        if not compra_id:
            return redirect('compras:lista_compras')

#Ahora van los datos del detalle
        producto = request.POST.get('id_id_producto')
        cantidad = request.POST.get('id_cantidad_detalle')
        precio = request.POST.get('id_precio_detalle')
        sub_total_detalle = request.POST.get('id_sub_total_detalle')
        descuento_detalle = request.POST.get('id_descuento_detalle')
        total_detalle = request.POST.get('id_total_detalle')

        prod = Productos.objects.get(pk=producto)

        det = ComprasDetalle(
            compra = enc,
            producto = prod,
            cantidad = cantidad,
            precio_comp = precio,
            sub_total = sub_total_detalle,
            descuento = descuento,
            total = total,
            creador = request.user
        )
    #Si se han obtenido los datos, lo guardamos
        if det:
            det.save()
            sub_total = ComprasDetalle.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento = ComprasDetalle.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            enc.descuento = descuento["descuento__sum"]
            enc.save()
        
        return redirect('compras:editar_compras', compra_id=compra_id)

    return render(request, template_name, contexto)
from django import forms
from .models import *

class FormProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields=['nombre', 'direccion', 'contacto', 'telefono', 'email', 'estado']
        widget = {'descripcion':forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class FormCompraEnc(forms.ModelForm):
    fecha_compra = forms.DateInput()
    fecha_factura = forms.DateInput()
    

    class Meta:
        model = ComprasEncabezado
        fields = [
            'proveedor', 'fecha_compra',
            'observaciones', 'no_fact', 'fecha_factura', 'sub_total','descuento', 'iva', 'total'
        ]
    #Cambiamos los atributos de los objetos que conforman el form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
        
        #Convertimos los campos a solo lectura
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['iva'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
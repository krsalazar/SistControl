from django import forms
from .models import *

class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categorias
        fields=['nombre', 'estado']
        labels = {'nombre':'Nombre categoria', 'estado':'Activo/Inactivo'}
        widget = {'descripcion':forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class FormSubCategoria(forms.ModelForm):
    #Muestra solo las categorias activas
    categoria = forms.ModelChoiceField(queryset=Categorias.objects.filter(estado=True).order_by('nombre'))
    class Meta:
        model = SubCategoria
        fields=['categoria', 'nombre', 'estado']
        labels = {'nombre':'Subcategoria', 'estado':'Activo/Inactivo'}
        widget = {'descripcion':forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
            self.fields['categoria'].empty_label = "Selecciona la categoría"

class FormMarca(forms.ModelForm):
    class Meta:
        model = Marcas
        fields=['nombre', 'estado']
        labels = {'nombre':'Marca', 'estado':'Activo/Inactivo'}
        widget = {'descripcion':forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class FormUm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields=['nombre', 'estado']
        labels = {'nombre':'UM', 'estado':'Activo/Inactivo'}
        widget = {'descripcion':forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class FormProductos(forms.ModelForm): 
    class Meta:
        model=Productos
        fields=['codigo','codigo_barra','nombre','estado', \
                'precio','existencia','ultima_compra',
                'marca','subcategoria','unidad_medida']
        exclude = ['modificador','updated','creador','created']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencia'].widget.attrs['readonly'] = True

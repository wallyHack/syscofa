
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        # campos que muestra el formulario
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción de la Categoría', 'estado':'Estado'}
        widget={
            'descripcion':forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model = SubCategoria
        # campos que muestra el formulario
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion': 'Sub Categoría', 'estado':'Estado'}
        widget={
            'descripcion':forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = "Selecciona categoria"

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        # campos que muestra el formulario
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción de la Marca', 'estado':'Estado'}
        widget={
            'descripcion':forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class UMForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        # campos que muestra el formulario
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripción de la Unidad de Medida', 'estado':'Estado'}
        widget={
            'descripcion':forms.TextInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # campos que muestra el formulario
        fields = [
            'codigo', 'codigo_barra', 'descripcion', 'estado', \
            'precio', 'existencia', 'ultima_compra', \
            'marca', 'subcategoria', 'unidad_medida'
        ] 
        exclude =['fc', 'fm', 'uc', 'um']
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        # campos de solo lectura
        self.fields['ultima_compra'].widget.attrs['read_only'] = True
        self.fields['existencia'].widget.attrs['read_only'] = True

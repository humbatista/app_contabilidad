from tkinter import Widget
from django import forms
from .models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'categoria', 'codigo', 'moneda_costo', 
        'metodo_costo','moneda','descripcion','entrada','precio',
        'tarifa','item_lista_de_precios','cuenta_de_gasto','cuenta_de_ingreso',
        'cuenta_de_entrada_inventario','cuenta_de_salida_inventario','proveedores')

        proveedores = forms.ModelMultipleChoiceField(
            queryset=Proveedores.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedores
        fields = ('__all__')
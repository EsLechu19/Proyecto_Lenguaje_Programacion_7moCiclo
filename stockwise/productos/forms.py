from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'precio',
            'stock',
            'stock_minimo',
            'categoria'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'stock': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'stock_minimo': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
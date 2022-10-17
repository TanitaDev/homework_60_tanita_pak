from django import forms

from webapp.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'remainder', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 73, 'rows': 5, 'class': ''})
        }

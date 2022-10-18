from django import forms

from webapp.models import *


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'remainder', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 73, 'rows': 5, 'class': ''})
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class AddToCartForm(forms.ModelForm):
    def save(self, product):
        instance = super(AddToCartForm, self).save(commit=False)
        instance.product = product
        instance.save()
        return instance

    class Meta:
        model = Cart
        fields = "__all__"

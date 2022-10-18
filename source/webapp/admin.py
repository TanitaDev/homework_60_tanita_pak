from django.contrib import admin
from django.utils.safestring import mark_safe

from webapp.models import Product, Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'category', 'remainder', 'price']
    search_fields = ['name', 'description']


class CartAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
    fields = ['product', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)

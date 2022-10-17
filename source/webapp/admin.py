from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image', 'category', 'remainder', 'price']
    search_fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)

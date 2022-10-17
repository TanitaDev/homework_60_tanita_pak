from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "products"
    model = Product
    ordering = ["category", "name"]

    paginate_by = 4
    paginate_orphans = 1


class ProductView(DetailView):
    template_name = "product.html"
    model = Product


class ProductCreate(CreateView):
    template_name = 'add_product.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    template_name = 'edit.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDelete(DeleteView):
    template_name = 'delete.html'
    model = Product
    success_url = reverse_lazy('index')

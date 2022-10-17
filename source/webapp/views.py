from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "products"
    model = Product
    ordering = ["category", "name"]


class ProductView(DetailView):
    template_name = "product.html"
    model = Product


class ProductCreate(CreateView):
    template_name = 'article/create.html'
    model = Product

    def get_redirect_url(self):
        return reverse('product.html', kwargs={'pk': self.object.pk})


def product_edit_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        context = {
            "products": products
        }
        return render(request, 'edit.html', context)
    elif request.method == "POST":
        products.name = request.POST.get("name")
        products.description = request.POST.get("description")
        products.image = request.POST.get("image")
        products.remainder = request.POST.get("remainder")
        products.price = request.POST.get("price")
        products.save()
        return redirect('/')


def delete_product_view(request, pk):
    products = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'products': products})
    elif request.method == 'POST':
        products.delete()
        return redirect('/')

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Product


class Index_view(ListView):
    pass


def index_view(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.order_by('category', 'name').filter(name__icontains=search_query).exclude(remainder='0')
        context = {
            'products': products
        }
        return render(request, 'index.html', context)
    else:
        products = Product.objects.order_by("category", "name")
        context = {
            'products': products
        }
        return render(request, 'index.html', context)


def single_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product.html', context)


def product_add_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    if request.method == "GET":
        return render(request, "add_product.html", context)
    elif request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.POST.get("image")
        category = request.POST.get("category")
        remainder = request.POST.get("remainder")
        price = request.POST.get("price")
        Product.objects.create(name=name, description=description, image=image, category=category, remainder=remainder, price=price)
        return redirect('/')


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

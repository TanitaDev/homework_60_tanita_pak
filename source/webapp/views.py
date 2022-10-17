from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "products"
    model = Product
    ordering = ["category", "name"]

    paginate_by = 4
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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

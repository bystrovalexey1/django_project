from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

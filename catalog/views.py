from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
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


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:product_create')

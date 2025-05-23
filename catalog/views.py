from django.core.exceptions import PermissionDenied
from django.http import request, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category
from users.models import CustomUser


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.has_perm('catalog.delete_product'):
            return self.form_class
        raise PermissionDenied


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class PublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden('У вас нет права снимать продукт с публикации')
        if not product.is_published:
            product.is_published = True
        else:
            product.is_published = False
        product.save()

        return redirect('catalog:product_detail', pk=product_pk)


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"

    def get_queryset(self):
        return Product.objects.filter(is_published=True)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_class_queryset(self, request):
        queryset = Product.objects.all()
        if not request.user.has_perm('catalog.can_unpublish_product'):
            queryset = Product.objects.filter(is_published=True)
        return queryset


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ContactTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:product_create')

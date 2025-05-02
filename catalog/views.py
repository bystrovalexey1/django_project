from django.shortcuts import render

from catalog.models import Product


def catalog_home(requests):
    product = Product.objects.all()
    context = {"product": product}
    return render(requests, "catalog/home.html", context=context)


def catalog_contacts(requests):
    return render(requests, "catalog/contacts.html")


def catalog_products(requests):
    product = Product.objects.all()
    context = {"product": product}
    return render(requests, "catalog/products.html", context=context)


def catalog_index(requests):
    product = Product.objects.all()
    context = {"product": product}
    return render(requests, "catalog/index.html", context=context)


def catalog_product_detail(requests, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(requests, "catalog/product_detail.html", context=context)

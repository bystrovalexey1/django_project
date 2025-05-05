from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    catalog_home,
    catalog_contacts,
    catalog_products,
    catalog_index,
    catalog_product_detail,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", catalog_home, name="home"),
    path("contacts/", catalog_contacts, name="contacts"),
    path("products/", catalog_products, name="products"),
    path("index/", catalog_index, name="index"),
    path(
        "product_detail/<int:product_id>/",
        catalog_product_detail,
        name="product_detail",
    ),
]

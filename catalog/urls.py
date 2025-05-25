from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, HomeListView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryCreateView, PublishProductView, ProductCategory

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeListView.as_view(), name="home"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("product_list/", ProductListView.as_view(), name="product_list"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("category_create/", CategoryCreateView.as_view(), name="category_create"),
    path("product_publish/<int:product_pk>/", PublishProductView.as_view(), name="product_publish"),
    path("product_list_category/<int:pk>/", ProductCategory.as_view(), name="product_category"),
]

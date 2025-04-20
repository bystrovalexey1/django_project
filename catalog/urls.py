from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import catalog_home, catalog_contacts


app_name = CatalogConfig.name


urlpatterns = [
    path("", catalog_home, name="home"),
    path("contacts/", catalog_contacts, name="contacts")
]

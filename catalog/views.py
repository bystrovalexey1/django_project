from django.shortcuts import render


def catalog_home(requests):
    return render(requests, "catalog/home.html")


def catalog_contacts(requests):
    return render(requests, "catalog/contacts.html")

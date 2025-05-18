from django import forms
from django.core.exceptions import ValidationError

from .models import Product, Category

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'is_published']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название товара'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание товара'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control input-group-text',
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control btn btn-outline-info dropdown-toggle',
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control input-group-text',
            'placeholder': 'Введите цену товара $'
        })

        self.fields['is_published'].widget.attrs.update({
            'class': 'form-check form-check-input',
            'role': 'switch',
        })



    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена должна быть положительной')
        return price

    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in name:
                self.add_error('name', f'Нельзя использовать слова: {FORBIDDEN_WORDS}')
        return name

    def clean_description(self):
        cleaned_data = super().clean()
        description = cleaned_data.get('description')

        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in description:
                self.add_error('description', f'Нельзя использовать слова: {FORBIDDEN_WORDS}')
        return description


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название категории'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание категории'
        })

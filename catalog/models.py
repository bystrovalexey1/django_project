from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(null=True, blank=True, verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["id"]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="изображение"
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name="product",
        verbose_name="категория",
    )
    price = models.IntegerField(verbose_name="цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата последнего изменения"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано",
    )
    owner = models.ForeignKey(
        CustomUser,
        verbose_name='Автор',
        help_text='Укажите автора',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.id} {self.name} - {self.description}. Цена: {self.price}$. Категория: {self.category}"

    class Meta:
        permissions = [
            ('can_unpublish_product', 'can unpublish product')
        ]
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["id"]

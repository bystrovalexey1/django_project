from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    note = models.TextField(null=True, blank=True, verbose_name="содержимое")
    image = models.ImageField(
        upload_to="blog/", blank=True, null=True, verbose_name="превью"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата публикации")
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество просмотров",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["-created_at"]

from django.db import models

NULLABLE = {"null": True, "blank": True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    slug = models.CharField(max_length=150, verbose_name="slug", **NULLABLE)
    body = models.TextField(verbose_name="содержимое")
    image = models.ImageField(
        upload_to="product/", verbose_name="изображение", **NULLABLE
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=True, verbose_name="опубликовано")
    views_count = models.IntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"

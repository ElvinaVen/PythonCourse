from django.db import models, connection

NULLABLE = {"null": True, "blank": True}


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(
        upload_to="product/", verbose_name="Изображение", **NULLABLE
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Наименование категории",
        related_name='categories'
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(verbose_name="Дата создания (записи в БД)")
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения (записи в БД)")


    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = (
            "price",
            "category",
            "created_at",
            "updated_at",
        )


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(**NULLABLE, verbose_name="Описание категории")

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

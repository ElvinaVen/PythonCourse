from django.db import models, connection

from users.models import User

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
        related_name="categories",
    )
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(verbose_name="Дата создания (записи в БД)")
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения (записи в БД)"
    )
    owner = models.ForeignKey(User, verbose_name='Владелец',help_text='Укажите владельца продукта', blank=True, null=True, on_delete=models.SET_NULL)

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
            cursor.execute(
                f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE"
            )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Version(models.Model):
    product = models.ForeignKey(
        "Product",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="продукт",
        related_name="versions",
    )
    version_number = models.IntegerField(verbose_name="Номер версии")
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    current_version_indicator = models.BooleanField(default=False, verbose_name="признак текущей версии")

    def __str__(self):
        return f"{self.version_number} - {self.version_name}"

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"


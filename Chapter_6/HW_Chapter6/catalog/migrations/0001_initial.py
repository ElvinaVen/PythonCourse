# Generated by Django 5.0.6 on 2024-05-27 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Наименование категории"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание категории"
                    ),
                ),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите наименование продукта",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                ("description", models.TextField(verbose_name="Описание продукта")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="product/",
                        verbose_name="Изображение",
                    ),
                ),
                ("price", models.IntegerField(verbose_name="Цена за покупку")),
                (
                    "created_at",
                    models.DateField(verbose_name="Дата создания (записи в БД)"),
                ),
                (
                    "updated_at",
                    models.DateField(
                        verbose_name="Дата последнего изменения (записи в БД)"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="categories",
                        to="catalog.category",
                        verbose_name="Наименование категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
                "ordering": ("price", "category", "created_at", "updated_at"),
            },
        ),
    ]

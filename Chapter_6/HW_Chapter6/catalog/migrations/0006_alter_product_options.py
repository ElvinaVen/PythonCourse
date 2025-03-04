# Generated by Django 4.2.13 on 2024-07-07 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("price", "category", "created_at", "updated_at"),
                "permissions": [
                    ("can_edit_description", "Can edit description"),
                    ("can_edit_category", "Can edit category"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]

# Generated by Django 4.2.13 on 2024-07-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("price", "category", "created_at", "updated_at"),
                "permissions": [
                    ("can_edit_description", "Can edit description"),
                    ("can_edit_category", "Can edit category"),
                    ("can_edit_is_published", "Can edit is_published"),
                ],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="Публикация"
            ),
        ),
    ]

# Generated by Django 5.1 on 2024-08-09 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="url_video",
            field=models.URLField(blank=True, null=True),
        ),
    ]

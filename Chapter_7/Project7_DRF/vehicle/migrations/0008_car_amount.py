# Generated by Django 5.0.6 on 2024-08-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0007_car_owner_moto_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="amount",
            field=models.IntegerField(default=1000, verbose_name="цена"),
        ),
    ]

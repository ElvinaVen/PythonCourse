# Generated by Django 5.0.6 on 2024-06-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='email'),
        ),
    ]
# Generated by Django 4.2.2 on 2024-07-31 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('deactivate_user', 'Can deactivate user'), ('view_all_users', 'Can view all users')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]

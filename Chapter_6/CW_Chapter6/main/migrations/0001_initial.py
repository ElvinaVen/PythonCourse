# Generated by Django 5.0.7 on 2024-07-25 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=100, verbose_name='тема письма')),
                ('message_body', models.TextField(verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter_name', models.CharField(max_length=150, verbose_name='Название рассылки')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='время начала рассылки')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='время окончания рассылки')),
                ('periodicity', models.CharField(choices=[('month', 'раз в месяц'), ('day', 'раз в день'), ('week', 'раз в неделю')], default='month', max_length=100, verbose_name='периодичность')),
                ('status', models.CharField(choices=[('запущена', 'запущена'), ('создана', 'создана'), ('завершена', 'завершена')], default='создана', max_length=100, verbose_name='статус рассылки')),
                ('client', models.ManyToManyField(to='main.client', verbose_name='Имена клиентов')),
                ('message', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.message', verbose_name='сообщение для клиентов')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='Дата и время попытки отправки')),
                ('status', models.CharField(choices=[('Успешно', 'Успешно'), ('Неуспешно', 'Неуспешно')], max_length=50, verbose_name='Cтатус рассылки')),
                ('server_response', models.CharField(blank=True, max_length=150, null=True, verbose_name='Ответ сервера почтового сервиса')),
                ('newsletter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.newsletter', verbose_name='рассылка для логов')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]

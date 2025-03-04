# Generated by Django 5.1 on 2024-08-09 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                    "course_name",
                    models.CharField(max_length=100, verbose_name="Название курса"),
                ),
                (
                    "course_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="learning/image_course",
                        verbose_name="превью  курса",
                    ),
                ),
                (
                    "course_description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание курса"
                    ),
                ),
            ],
            options={
                "verbose_name": "курс",
                "verbose_name_plural": "курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
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
                    "lesson_name",
                    models.CharField(max_length=100, verbose_name="Название урока"),
                ),
                (
                    "lesson_description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание урока"
                    ),
                ),
                (
                    "lesson_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="learning/image_lesson",
                        verbose_name="превью  урока",
                    ),
                ),
                ("url_video", models.URLField()),
                (
                    "course_name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="learning.course",
                        verbose_name="курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "урок",
                "verbose_name_plural": "уроки",
            },
        ),
    ]

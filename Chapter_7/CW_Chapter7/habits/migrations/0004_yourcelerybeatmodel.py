# Generated by Django 5.1.1 on 2024-10-05 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_alter_habit_time_to_complete"),
    ]

    operations = [
        migrations.CreateModel(
            name="YourCeleryBeatModel",
            fields=[
                (
                    "habit_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="habits.habit",
                    ),
                ),
            ],
            bases=("habits.habit",),
        ),
    ]

from django.contrib import admin
from habits.models import Habit


# Register your models here.
admin.site.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "place",
        "time",
        "action",
        "nice_habit",
        "associated_habit",
        "periodicity",
        "surprise",
        "time_to_complete",
        "is_published",

    )



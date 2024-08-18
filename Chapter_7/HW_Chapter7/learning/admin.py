from django.contrib import admin

from learning.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_name",
        "course_image",
        "course_description",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "lesson_name",
        "lesson_description",
        "lesson_image",
        "url_video",
        "course",
    )

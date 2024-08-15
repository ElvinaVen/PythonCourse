from django.db import models

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    course_name = models.CharField(max_length=100, verbose_name="Название курса")
    course_image = models.ImageField(
        upload_to="learning/image_course", verbose_name="превью  курса", **NULLABLE
    )
    course_description = models.TextField(**NULLABLE, verbose_name="Описание курса")

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100, verbose_name="Название урока")
    lesson_description = models.TextField(**NULLABLE, verbose_name="Описание урока")
    lesson_image = models.ImageField(
        upload_to="learning/image_lesson", verbose_name="превью  урока", **NULLABLE
    )
    url_video = models.URLField(max_length=200, **NULLABLE)
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="lessons",
        verbose_name="курс",
        **NULLABLE,
    )

    def __str__(self):
        return f"Урок {self.lesson_name} из курса {self.course}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

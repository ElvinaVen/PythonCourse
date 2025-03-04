from django.contrib.auth.models import AbstractUser
from django.db import models

from learning.models import Course, Lesson


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="телефон",
        null=True,
        blank=True,
        help_text="введите номер телефона",
    )
    city = models.CharField(
        max_length=23,
        verbose_name="город",
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="аватар", null=True, blank=True
    )
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):

    PAYMENT_CASH = "cash"
    PAYMENT_TRANSFER = "transfer"
    PAYMENT_CHOICES = (
        (PAYMENT_CASH, "Оплата наличными"),
        (PAYMENT_TRANSFER, "Безналичная оплата"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_payment",
        verbose_name="пользователь",
    )
    payment_date = models.DateField(verbose_name="дата оплаты", auto_created=True, blank=True, null=True)
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        blank=True,
        null=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="оплаченный урок",
        blank=True,
        null=True,
    )
    payment_amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="сумма оплаты"
    )
    payment_type = models.CharField(
        choices=PAYMENT_CHOICES, verbose_name="способ оплаты:"
    )
    session_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Id сессии")
    payment_link = models.URLField(max_length=400, blank=True, null=True, verbose_name="Ссылка на оплату")

    def __str__(self):
        return f"{self.user} - {self.paid_lesson if self.paid_lesson else self.paid_course}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

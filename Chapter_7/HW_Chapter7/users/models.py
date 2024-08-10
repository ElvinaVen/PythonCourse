from django.contrib.auth.models import AbstractUser
from django.db import models


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

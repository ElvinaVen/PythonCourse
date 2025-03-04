from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта", max_length=255)

    phone = models.CharField(max_length=35, unique=True, verbose_name="Телефон", blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name="аватар", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

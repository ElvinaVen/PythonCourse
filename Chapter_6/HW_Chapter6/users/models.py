from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="users/", verbose_name='аватар', null=True, blank=True)
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='телефон', null=True, blank=True, help_text='введите номер телефона')
    country = models.CharField(max_length=23, verbose_name='страна')
    token = models.CharField(max_length=100, verbose_name='токен', null=True, blank=True)
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

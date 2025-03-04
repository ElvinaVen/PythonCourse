from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='телефон', null=True, blank=True,
                                    help_text='введите номер телефона')
    country = models.CharField(max_length=23, verbose_name='страна')
    token = models.CharField(max_length=100, verbose_name='токен', null=True, blank=True)
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = [
            ('deactivate_user', 'Can deactivate user'),
            ('view_all_users', 'Can view all users'),
        ]

    def __str__(self):
        return self.email

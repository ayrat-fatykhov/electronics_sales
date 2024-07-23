from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Определяет поля для модели 'Пользватель'.
    Реализуют возможность взаимодействия с пользователем через email.
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField(default=True, verbose_name='активность')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

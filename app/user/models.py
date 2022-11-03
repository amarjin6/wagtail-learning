from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from core.enums import Gender, Role


class User(AbstractUser):
    gender = models.CharField(
        max_length=15,
        choices=Gender.choices(),
        default=Gender.DEFAULT.name,
        null=True,
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,12}$',
                                 message="Phone number must be entered in the format: '+XXX-XX-XXX-XX-XX',"
                                         " e.g. +375291234567.")

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=13,
        null=True,
        blank=False,
    )

    university = models.ForeignKey(
        'university.University',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='user_university',
    )

    requested_role = models.CharField(
        max_length=9,
        choices=Role.choices(),
        default=Role.DEFAULT.name,
        null=True,
    )

    first_name = models.CharField(
        max_length=64,
        null=True,
    )

    last_name = models.CharField(
        max_length=64,
        null=True,
    )

    username = models.CharField(
        max_length=32,
        unique=True,
        null=True,
    )

    email = models.EmailField(
        unique=True,
        null=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']

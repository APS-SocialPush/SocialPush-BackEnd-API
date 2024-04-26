from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

import pytz


class CustomUser(AbstractUser):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    username = None
    email = models.EmailField(_("email address"), unique=True)

    photo = models.ImageField(
        verbose_name="Foto do usuário",
        upload_to="fotos/",
        null=True,
        blank=True,
    )

    timezone = models.CharField(
        verbose_name="Fuso horário",
        max_length=32,
        choices=TIMEZONES,
        default='UTC'
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        """Retorna a representação do objeto como string."""
        return self.email

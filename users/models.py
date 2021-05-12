from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):

    level = models.CharField(
        max_length=15, choices=settings.DIFFICULTY_CHOICES, default="beginner"
    )
    learning_language = models.CharField(
        max_length=2, choices=settings.LANGUAGE_CHOICES, default="en"
    )

    def __str__(self):
        return self.email

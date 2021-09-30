from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import phone_validator


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        UNSET = 'MF', 'Unset'

    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSET)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

    @property
    def is_benefactor(self):
        return hasattr(self, 'benefactor')

    @property
    def is_charity(self):
        return hasattr(self, 'charity')

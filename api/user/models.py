from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class CustomUser(models.Model):
    class Type(models.TextChoices):
        SUPERADMIN = 1, _('Супер-Админ')
        ADMIN = 2, _('Админ')
        TEACHER = 3, _('Преподаватель')

    role = models.CharField(max_length=255, choices=Type.choices)


class Teacher(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    description = models.TextField()
    mail = models.CharField(max_length=128)
    phone = models.CharField(max_length=10)
    tg_username = models.CharField(max_length=64)


class Admin(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.CASCADE)
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)


class University(models.Model):
    name = models.CharField(max_length=255)

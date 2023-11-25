from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class CustomUser(models.Model):
    class Type(models.TextChoices):
        SUPERADMIN = 1, _('Супер-Админ')
        ADMIN = 2, _('Админ')
        TEACHER = 3, _('Преподаватель')

    login = models.CharField(max_length=128, null=False, blank=False)
    password = models.TextField(null=False, blank=False)
    role = models.CharField(max_length=1, choices=Type.choices, null=False, blank=False)


class Teacher(models.Model):
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, null=False, blank=False)
    user = models.ForeignKey('user.CustomUser', on_delete=models.DO_NOTHING, null=False, blank=False)
    first_name = models.CharField(max_length=128, null=False, blank=False)
    last_name = models.CharField(max_length=128, null=False, blank=False)
    middle_name = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(default=None)
    mail = models.CharField(max_length=128, null=False, blank=False)
    phone = models.CharField(max_length=10, default=None)
    tg_username = models.CharField(max_length=64, default=None)


class Admin(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.DO_NOTHING, null=False, blank=False)
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, null=False, blank=False)
    first_name = models.CharField(max_length=128, null=False, blank=False)
    last_name = models.CharField(max_length=128, null=False, blank=False)
    middle_name = models.CharField(max_length=128, null=False, blank=False)


class University(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

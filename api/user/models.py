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

    def __str__(self) -> str:
        return f"{self.login}: {self.get_role_display()}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural= 'Пользователи'


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

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.university}"

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural= 'Преподаватели'


class Admin(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.DO_NOTHING, null=False, blank=False)
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, null=False, blank=False)
    first_name = models.CharField(max_length=128, null=False, blank=False)
    last_name = models.CharField(max_length=128, null=False, blank=False)
    middle_name = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.university}"

    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural= 'Админы'


class University(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural= 'Университеты'

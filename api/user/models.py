from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class CustomUser(models.Model):
    class Type(models.TextChoices):
        SUPERADMIN = 1, _('Супер-Админ')
        ADMIN = 2, _('Админ')
        TEACHER = 3, _('Преподаватель')

    login = models.CharField(max_length=128, null=False, blank=False, verbose_name='Логин')
    password = models.TextField(null=False, blank=False, verbose_name='Пароль')
    role = models.CharField(max_length=1, choices=Type.choices, null=False, blank=False, verbose_name='Роль')

    def __str__(self) -> str:
        return f"{self.login}: {self.get_role_display()}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural= 'Пользователи'


class Teacher(models.Model):
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Университет')
    user = models.ForeignKey('user.CustomUser', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Пользователь')
    first_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Отчетсво')
    description = models.TextField(default=None, verbose_name='Описание')
    mail = models.CharField(max_length=128, null=False, blank=False, verbose_name='Почта')
    phone = models.CharField(max_length=10, default=None, verbose_name='Номер телефона')
    tg_username = models.CharField(max_length=64, default=None, verbose_name='tg аккаунт')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.university}"

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural= 'Преподаватели'


class Admin(models.Model):
    user = models.ForeignKey('user.CustomUser', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Пользователь')
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Университет')
    first_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Отчество')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.university}"

    class Meta:
        verbose_name = 'Админ'
        verbose_name_plural= 'Админы'


class University(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Название университета')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Университет'
        verbose_name_plural= 'Университеты'

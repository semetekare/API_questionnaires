from django.db import models
from django.utils.translation import gettext_lazy as _



class Subject(models.Model):
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Университет')
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='Название дисциплины')

    def __str__(self) -> str:
        return f"{self.title}: {self.university}"

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural= 'Дисциплины'


class Student(models.Model):
    first_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=128, null=False, blank=False, verbose_name='Отчество')
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, verbose_name='Университет')
    group = models.CharField(max_length=128, null=False, blank=False, verbose_name='Группа')
    tg_username = models.CharField(max_length=64, null=False, blank=False, verbose_name='tg аккаунт')

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}: {self.tg_username} {self.university}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural= 'Студенты'


class StudentsGroup(models.Model):
    university = models.ForeignKey('user.University', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Университет')
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='Название группы')

    def __str__(self) -> str:
        return f"{self.title}: {self.university}"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural= 'Группы'


class StudentsGroupsSubjects(models.Model):
    subject = models.ForeignKey('student.Subject', on_delete=models.DO_NOTHING, null=False, blank=False)
    students_group = models.ForeignKey('student.StudentsGroup', on_delete=models.DO_NOTHING, null=False, blank=False)


class StudentsGroupsStudents(models.Model):
    students_group = models.ForeignKey('student.StudentsGroup', on_delete=models.DO_NOTHING, null=False, blank=False)
    student = models.ForeignKey('student.Student', on_delete=models.DO_NOTHING, null=False, blank=False)

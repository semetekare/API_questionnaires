from django.db import models
from django.utils.translation import gettext_lazy as _



class Statistic(models.Model):
    class Type(models.TextChoices):
        correct = 1, _('Студент ответил на вопрос правильно')
        incorrect = 2, _('Студент ответил на вопрос неправильно')
        missed = 3, _('Студент пропустил этот вопрос')

    test = models.ForeignKey('question.Test', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Тест')
    student = models.ForeignKey('student.Student', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Студент')
    question = models.ForeignKey('question.Question', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Вопрос')
    needed_time = models.IntegerField(null=False, blank=False, verbose_name='Время потраченно на ответ (в секундах)')
    type = models.CharField(max_length=1, choices=Type.choices, null=False, blank=False, verbose_name='Как студент поступил с вопросом')

    def __str__(self) -> str:
        return f"{self.test}; {self.student}; {self.question}; {self.type}"

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural= 'Статистики'


class StatisticsAnswers(models.Model):
    statistic = models.ForeignKey('statistic.Statistic', on_delete=models.DO_NOTHING, null=False, blank=False)
    answer = models.ForeignKey('question.Answer', on_delete=models.DO_NOTHING, null=False, blank=False)

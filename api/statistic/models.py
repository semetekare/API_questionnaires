from django.db import models
from django.utils.translation import gettext_lazy as _



class Statistic(models.Model):
    class Type(models.TextChoices):
        correct = 1, _('Студент ответил на вопрос правильно')
        incorrect = 2, _('Студент ответил на вопрос неправильно')
        missed = 3, _('Студент пропустил этот вопрос')

    test = models.ForeignKey('question.Test', on_delete=models.DO_NOTHING, null=False, blank=False)
    student = models.ForeignKey('student.Student', on_delete=models.DO_NOTHING, null=False, blank=False)
    question = models.ForeignKey('question.Question', on_delete=models.DO_NOTHING, null=False, blank=False)
    needed_time = models.IntegerField(null=False, blank=False)
    type = models.IntegerField(choices=Type.choices, null=False, blank=False)


class StatisticsAnswers(models.Model):
    statistic = models.ForeignKey('statistic.Statistic', on_delete=models.DO_NOTHING, null=False, blank=False)
    answer = models.ForeignKey('question.Answer', on_delete=models.DO_NOTHING, null=False, blank=False)

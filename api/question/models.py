from django.db import models
from django.utils.translation import gettext_lazy as _



class Test(models.Model):
    class Type(models.TextChoices):
        IMMEDIATELY = 1, _('сразу после прохождения теста')
        AFTER_PERMISSION = 2, _('после разрешения от препода')

    questions_base = models.ForeignKey('question.QuestionsBase', on_delete=models.DO_NOTHING, null=False, blank=False)
    is_actual = models.BooleanField(default=True, null=False, blank=False)
    finish_actual = models.IntegerField(default=None)
    title = models.TextField(null=False, blank=False)
    description = models.TextField(default=None)
    expires_in = models.IntegerField(null=False, blank=False)
    total_questions_quantity = models.IntegerField(null=False, blank=False)
    allow_pass_return = models.BooleanField(default=True, null=False, blank=False)
    warn = models.BooleanField(default=True, null=False, blank=False)
    when_to_show_statistic = models.CharField(max_length=1, choices=Type.choices)
    send_statistic = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.title}: {self.is_actual}; {self.questions_base}"

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural= 'Тесты'


class TestsQuestionsGroups(models.Model):
    test = models.ForeignKey('question.Test', on_delete=models.DO_NOTHING, null=False, blank=False)
    questions_group = models.ForeignKey('question.QuestionsGroup', on_delete=models.DO_NOTHING, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)


class QuestionsBase(models.Model):
    subject = models.ForeignKey('student.Subject', on_delete=models.DO_NOTHING, null=False, blank=False)
    title = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.title}; {self.subject}"

    class Meta:
        verbose_name = 'База вопросов'
        verbose_name_plural= 'Базы вопросов'


class QuestionsGroup(models.Model):
    questions_base = models.ForeignKey('question.QuestionsBase', on_delete=models.DO_NOTHING, null=False, blank=False)
    title = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.title}; {self.questions_base}"

    class Meta:
        verbose_name = 'Группа вопросов'
        verbose_name_plural= 'Группы вопросов'


class Question(models.Model):
    class Type(models.TextChoices):
        SINGLE = 1, _('единичный ответ')
        MULTIPLE = 2, _('множественный ответ')
        CALCULATION = 3, _('расчетное задание')

    questions_group = models.ForeignKey('question.QuestionsGroup', on_delete=models.DO_NOTHING, null=False, blank=False)
    formulation = models.TextField(null=False, blank=False)
    type = models.CharField(max_length=1, choices=Type.choices, null=False, blank=False)
    ok_comment = models.CharField(max_length=128, default=None)
    bad_comment = models.CharField(max_length=128, default=None, blank=True)
    shuffle_answers = models.BooleanField(default=False)
    cost = models.FloatField(default=0.1, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.formulation}: {self.type}; {self.questions_group}"

    class Meta:
        verbose_name = 'База вопросов'
        verbose_name_plural= 'Базы вопросов'


class Answer(models.Model):
    question = models.ForeignKey('question.Question', on_delete=models.DO_NOTHING, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    is_correct = models.BooleanField(null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.text}: {self.is_correct}; {self.question}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural= 'Ответы'


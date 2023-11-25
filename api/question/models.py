from django.db import models
from django.utils.translation import gettext_lazy as _



class Test(models.Model):
    class Type(models.TextChoices):
        IMMEDIATELY = 1, _('сразу после прохождения теста')
        AFTER_PERMISSION = 2, _('после разрешения от препода')

    questions_base = models.ForeignKey('question.QuestionsBase', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='База вопросов')
    is_actual = models.BooleanField(default=True, null=False, blank=False, verbose_name='Является ли тест актуальным')
    finish_actual = models.IntegerField(default=None, verbose_name='Через сколько тест станет недоступен (в секундах)')
    title = models.TextField(null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(default=None, verbose_name='Описание')
    expires_in = models.IntegerField(null=False, blank=False, verbose_name='Время на тест (в секундах)')
    total_questions_quantity = models.IntegerField(null=False, blank=False, verbose_name='Сколько вопросов будет взято и базы вопросов')
    allow_pass_return = models.BooleanField(default=True, null=False, blank=False, verbose_name='Разрешить пропускать или возвращаться к вопросам')
    warn = models.BooleanField(default=True, null=False, blank=False, verbose_name='Показывать ли предупреждение о том, что не все вопросы отвечены')
    when_to_show_statistic = models.CharField(max_length=1, choices=Type.choices, verbose_name='Когда показывать статистику')
    send_statistic = models.BooleanField(default=True, null=False, blank=False, verbose_name='Отправить результаты теста на почту преподователю')

    def __str__(self) -> str:
        return f"{self.title}: {self.is_actual}; {self.questions_base}"

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural= 'Тесты'


class TestsQuestionsGroups(models.Model):
    test = models.ForeignKey('question.Test', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Тест')
    questions_group = models.ForeignKey('question.QuestionsGroup', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Группа вопросов')
    quantity = models.IntegerField(null=False, blank=False, verbose_name='кол-во вопросов, которое должны взять из базы вопросов')


class QuestionsBase(models.Model):
    subject = models.ForeignKey('student.Subject', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Дисциплина')
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='Название')

    def __str__(self) -> str:
        return f"{self.title}; {self.subject}"

    class Meta:
        verbose_name = 'База вопросов'
        verbose_name_plural= 'Базы вопросов'


class QuestionsGroup(models.Model):
    questions_base = models.ForeignKey('question.QuestionsBase', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='База вопросов')
    title = models.CharField(max_length=128, null=False, blank=False, verbose_name='Название')

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

    questions_group = models.ForeignKey('question.QuestionsGroup', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Группа вопросов')
    formulation = models.TextField(null=False, blank=False, verbose_name='Формулировка')
    type = models.CharField(max_length=1, choices=Type.choices, null=False, blank=False, verbose_name='Тип')
    ok_comment = models.CharField(max_length=128, default=None, verbose_name='Коментарий в случае правильного ответа')
    bad_comment = models.CharField(max_length=128, default=None, blank=True, verbose_name='Коментарий в случае неправильного ответа')
    shuffle_answers = models.BooleanField(default=False, verbose_name='Перемешать варианты ответов')
    cost = models.FloatField(default=0.1, null=False, blank=False, verbose_name='Баллы за вопрос')

    def __str__(self) -> str:
        return f"{self.formulation}: {self.type}; {self.questions_group}"

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural= 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey('question.Question', on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Вопрос')
    text = models.TextField(null=False, blank=False, verbose_name='Текст')
    is_correct = models.BooleanField(null=False, blank=False, verbose_name='Правильный ли ответ')

    def __str__(self) -> str:
        return f"{self.text}: {self.is_correct}; {self.question}"

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural= 'Ответы'


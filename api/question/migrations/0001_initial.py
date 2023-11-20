# Generated by Django 4.2.7 on 2023-11-20 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.subject')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionsGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('questions_base', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='question.questionsbase')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_actual', models.BooleanField(default=True)),
                ('finish_actual', models.IntegerField(default=None)),
                ('title', models.TextField()),
                ('description', models.TextField(default=None)),
                ('expires_in', models.IntegerField()),
                ('total_questions_quantity', models.IntegerField()),
                ('allow_pass_return', models.BooleanField(default=True)),
                ('warn', models.BooleanField(default=True)),
                ('when_to_show_statistic', models.IntegerField(choices=[('1', 'сразу после прохождения теста'), ('2', 'после разрешения от препода')])),
                ('send_statistic', models.BooleanField(default=True)),
                ('questions_base', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='question.questionsbase')),
            ],
        ),
        migrations.CreateModel(
            name='TestsQuestionsGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('questions_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='question.questionsgroup')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='question.test')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formulation', models.TextField()),
                ('type', models.IntegerField(choices=[('1', 'единичный ответ'), ('2', 'множественный ответ'), ('3', 'расчетное задание')])),
                ('ok_comment', models.CharField(default=None, max_length=128)),
                ('bad_commnet', models.CharField(default=None, max_length=128)),
                ('shuffle_answers', models.BooleanField(default=False)),
                ('cost', models.FloatField(default=0.1)),
                ('questions_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='question.questionsgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='question.question')),
            ],
        ),
    ]

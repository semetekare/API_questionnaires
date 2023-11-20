from django.contrib import admin

from question.models import Test, TestsQuestionsGroups, QuestionsBase, QuestionsGroup, Question, Answer


admin.site.register(Test)
admin.site.register(TestsQuestionsGroups)
admin.site.register(QuestionsBase)
admin.site.register(QuestionsGroup)
admin.site.register(Question)
admin.site.register(Answer)

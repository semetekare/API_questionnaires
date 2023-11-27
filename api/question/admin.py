from django.contrib import admin

from question.models import Test, TestsQuestionsGroups, QuestionsBase, QuestionsGroup, Question, Answer


class TestAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('is_actual', 'when_to_show_statistic',)
admin.site.register(Test, TestAdmin)


admin.site.register(TestsQuestionsGroups)


class QuestionsBaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    list_display_links = ('title',)
    search_fields = ('title', 'subject',)
admin.site.register(QuestionsBase, QuestionsBaseAdmin)


class QuestionsGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'questions_base')
    list_display_links = ('title',)
    search_fields = ('title', 'questions_base',)
admin.site.register(QuestionsGroup, QuestionsGroupAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('type', 'formulation',)
    list_display_links = ('type', 'formulation',)
    search_fields = ('questions_group', 'ok_comment', 'bad_comment', 'formulation',)
    list_filter = ('questions_group',)
admin.site.register(Question)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'is_correct')
    list_display_links = ('text',)
    search_fields = ('text',)
    list_filter = ('is_correct',)
admin.site.register(Answer, AnswerAdmin)

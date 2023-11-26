from django.contrib import admin

from statistic.models import Statistic, StatisticsAnswers


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('test', 'student', 'question', 'type',)
    list_display_links = ('test', 'student', 'question',)
    search_fields = ('test', 'student', 'question',)
    list_filter = ('type',)
admin.site.register(Statistic, StatisticAdmin)


admin.site.register(StatisticsAnswers)

from django.contrib import admin

from student.models import Subject, Student, StudentsGroup, StudentsGroupsSubjects, StudentsGroupsStudents


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'university',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('university',)
admin.site.register(Subject, SubjectAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'group', 'university', 'tg_username',)
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name', 'tg_username',)
    list_filter = ('group', 'university',)
admin.site.register(Student, StudentAdmin)


class StudentsGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'university',)
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('university',)
admin.site.register(StudentsGroup, StudentsGroupAdmin)


admin.site.register(StudentsGroupsSubjects)
admin.site.register(StudentsGroupsStudents)

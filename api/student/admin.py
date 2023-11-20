from django.contrib import admin

from student.models import Subject, Student, StudentsGroup, StudentsGroupsSubjects, StudentsGroupsStudents


admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(StudentsGroup)
admin.site.register(StudentsGroupsSubjects)
admin.site.register(StudentsGroupsStudents)

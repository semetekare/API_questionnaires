from django.contrib import admin

from user.models import CustomUser, Admin, Teacher, University


admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(University)

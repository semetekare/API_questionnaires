from django.contrib import admin

from user.models import CustomUser, Admin, Teacher, University


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('login', 'role',)
    list_display_links = ('login',)
    search_fields = ('login',)
    list_filter = ('role',)
admin.site.register(CustomUser, CustomUserAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mail', 'phone', 'tg_username', 'university',)
    list_display_links = ('first_name', 'last_name', 'mail', 'phone', 'tg_username',)
    search_fields = ('first_name', 'last_name', 'mail', 'phone', 'tg_username', 'university',)
    list_filter = ('university',)
admin.site.register(Teacher, TeacherAdmin)


class AdminAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'university',)
    list_display_links = ('first_name', 'last_name',)
    search_fields = ('first_name', 'last_name', 'university',)
    list_filter = ('university',)
admin.site.register(Admin, AdminAdmin)


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
admin.site.register(University, UniversityAdmin)

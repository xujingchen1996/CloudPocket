from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import commonUser


# Register your models here.

class commonUserInline(admin.TabularInline):
    model = commonUser
    can_delete = False
    verbose_name_plural = 'commonUser'


class UserAdmin(BaseUserAdmin):
    inlines = (commonUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

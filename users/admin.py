from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from .models import User


@admin.register(User)
class UserAdmin(_UserAdmin):
    section1 = (None, {'fields': ('username', 'password', 'role')})
    fieldsets = (section1,) + _UserAdmin.fieldsets[1:]

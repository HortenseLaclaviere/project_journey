from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ParentUserAdmin
from .models import User


class UserAdmin(ParentUserAdmin):
    ordering = ("email",)


admin.site.register(User, UserAdmin)

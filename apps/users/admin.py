from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as ParentUserAdmin
from django.contrib.auth.models import User
from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(ParentUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    ordering = ("email",)
    fieldsets = (
        (
            "Informations personnelles",
            {"fields": ("username", "email", "password", "profile_picture")},
        ),
    )
    add_fieldsets = (
        (
            "Informations personnelles",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "profile_picture",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    list_display = ["username", "email", "is_superuser"]

    def message_user(
        self,
        request,
        message,
        level=messages.SUCCESS,
        extra_tags="",
        fail_silently=False,
    ):
        full_message = f"L'utilisateur.trice a bien été enregistré.e"
        return super().message_user(
            request, full_message, level, extra_tags, fail_silently
        )


admin.site.register(User, UserAdmin)

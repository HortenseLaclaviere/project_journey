from django.contrib import admin

from apps.choices.models import Choice


# Register your models here.
class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ("pk", "text")


admin.site.register(Choice, ChoiceAdmin)

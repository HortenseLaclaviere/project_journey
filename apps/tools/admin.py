from django.contrib import admin

from apps.tools.models import Tool


# Register your models here.
class ToolAdmin(admin.ModelAdmin):
    model = Tool
    list_display = ("pk", "name")


admin.site.register(Tool, ToolAdmin)

from django.contrib import admin
from apps.stories.models import Story


# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    model = Story
    list_display = ("pk", "text")


admin.site.register(Story, StoryAdmin)

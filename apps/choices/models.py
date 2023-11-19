from django.db import models

from apps.tools.models import Tool


class Choice(models.Model):
    text = models.CharField(max_length=255)
    tools_needed = models.ManyToManyField(Tool, blank=True)
    next_story = models.ForeignKey(
        "stories.Story", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.text

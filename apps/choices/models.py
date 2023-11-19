from django.db import models
from apps.stories.models import Stories
from apps.tools.models import Tools


class Choices(models.Model):
    text = models.CharField(max_length=255)
    tools_needed = models.ManyToManyField(Tools, blank=True)
    next_story = models.ForeignKey(
        Stories, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.text

from django.db import models
from apps.choices.models import Choices


class Stories(models.Model):
    text = models.TextField()
    choices_available = models.ManyToManyField(Choices, blank=True)

    def __str__(self):
        return self.text

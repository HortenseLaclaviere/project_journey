from django.db import models


class Story(models.Model):
    text = models.TextField()
    choices_available = models.ManyToManyField("choices.Choice", blank=True)

    def __str__(self):
        return self.text

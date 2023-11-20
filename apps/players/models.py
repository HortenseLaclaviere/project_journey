from django.db import models
from django.conf import settings


class Player(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    progression = models.ForeignKey("stories.Story", on_delete=models.PROTECT)
    player_tools = models.ManyToManyField("tools.Tool", blank=True)

    def __str__(self):
        return self.user

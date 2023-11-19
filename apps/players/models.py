from django.db import models
from apps.users.models import User


class Player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    progression = models.ForeignKey("Stories", on_delete=models.PROTECT)
    player_tools = models.ManyToManyField("Tools", blank=True)

    def __str__(self):
        return self.user_id

from django.db import models


class Player(models.Model):
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    progression = models.ForeignKey("stories.Story", on_delete=models.PROTECT)
    player_tools = models.ManyToManyField("tools.Tool", blank=True)

    def __str__(self):
        return self.user_id

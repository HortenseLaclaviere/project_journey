from django.db import models
from django.contrib.auth.models import User  # modèle User fournit par django


class Player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    progression = models.ForeignKey('Story', on_delete=models.PROTECT)
    player_objects = models.ForeignKey('Object', on_delete=models.PROTECT)

    def __str__(self):
        return self.user_id


class Story(models.Model):
    story_text = models.TextField()
    choices_available = models.ManyToManyField('Choice', blank=True)
    # 'Choice' entre '' car le modèle cible n'est pas encore défini au moment de la déclaration

    def __str__(self):
        return self.story_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    object_needed = models.IntegerField(blank=True, null=True)
    next_story = models.ForeignKey(Story, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.choice_text


class Object(models.Model):
    object_name = models.CharField(max_length=50)




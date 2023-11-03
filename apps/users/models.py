from django.db import models
from django.contrib.auth.models import User  # modèle User fournit par django


class Player(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    progression = models.ForeignKey("Story", on_delete=models.PROTECT)
    player_objects = models.ForeignKey("Object", on_delete=models.PROTECT)

    def __str__(self):
        return self.user_id

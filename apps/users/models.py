from django.contrib.auth.models import AbstractUser  # modèle User fournit par django
from django.db import models

from apps.users.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Pseudo"
    )
    profile_picture = models.ImageField(
        blank=True, null=True, verbose_name="Photo de profil"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

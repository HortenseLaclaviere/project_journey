from django.contrib.auth.models import AbstractUser  # modèle User fournit par django
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    nickname = models.CharField(max_length=55, verbose_name="Pseudo")
    profile_picture = models.ImageField(
        blank=True, null=True, verbose_name="Photo de profil"
    )

    USERNAME_FIELD = "email"

from django.db import models


class Tools(models.Model):
    name = models.CharField(max_length=50)

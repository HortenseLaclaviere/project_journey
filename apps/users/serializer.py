from .models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Un sérialiseur est utilisé pour convertir les objets du modèle en données JSON pour les API.

    class Meta:
        # La classe Meta permet de configurer le sérialiseur en spécifiant des métadonnées pour le modèle.
        model = User
        fields = ["url", "username", "email", "is_staff"]

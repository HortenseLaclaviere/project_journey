from django.contrib.auth.models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Cette classe définit un sérialiseur pour le modèle User. Un sérialiseur est utilisé pour convertir les objets
    # du modèle en données JSON (ou d'autres formats) pour les API.

    class Meta:
        # La classe Meta permet de configurer le sérialiseur en spécifiant des métadonnées pour le modèle.

        model = User
        # L'attribut model indique au sérialiseur quel modèle il doit sérialiser. Dans ce cas, il s'agit du modèle User.

        fields = ["url", "username", "email", "is_staff"]
        # L'attribut fields spécifie les champs du modèle User à inclure dans la sérialisation. Cela signifie que les
        # données JSON générées à partir d'un objet User incluront les champs "url", "username", "email" et "is_staff".

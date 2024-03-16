from .models import User
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Un sérialiseur est utilisé pour convertir les objets du modèle en données JSON pour les API.
    password = serializers.CharField(write_only=True)

    class Meta:
        # La classe Meta permet de configurer le sérialiseur en spécifiant des métadonnées pour le modèle.
        model = User
        fields = ["url", "username", "email", "is_staff", "password"]

    def create(self, validated_data):
        # Utilise create_user pour hasher le mot de passe correctement
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        # Gère la mise à jour du mot de passe correctement
        password = validated_data.pop("password", None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

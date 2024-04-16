from .models import User
from rest_framework import serializers
from django.utils.formats import date_format


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Un sérialiseur est utilisé pour convertir les objets du modèle en données JSON pour les API.
    password = serializers.CharField(write_only=True)
    format_date_joined = serializers.SerializerMethodField()

    class Meta:
        # La classe Meta permet de configurer le sérialiseur en spécifiant des métadonnées pour le modèle.
        model = User
        fields = [
            "url",
            "username",
            "email",
            "is_staff",
            "password",
            "format_date_joined",
        ]

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

    def get_format_date_joined(self, obj):
        return date_format(obj.date_joined, format="DATE_FORMAT", use_l10n=True)

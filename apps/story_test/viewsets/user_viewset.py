from django.contrib.auth.models import User
from rest_framework import viewsets

from apps.story_test.serializers.user_serializer import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # Cette classe définit un viewset pour le modèle User (généralement une classe Django de modèle de base de données).
    # Un viewset est un moyen pratique de créer une API CRUD pour ce modèle.

    queryset = User.objects.all()
    # queryset spécifie la source de données pour cette vue.
    # Dans ce cas, il récupère tous les enregistrements du modèle User depuis la base de données.

    serializer_class = UserSerializer
    # serializer_class spécifie la classe de sérialiseur à utiliser pour convertir les objets User en données JSON (
    # ou autres formats). Il doit être défini ailleurs dans le code de votre application et est responsable de la
    # conversion des objets User en données sérialisées.

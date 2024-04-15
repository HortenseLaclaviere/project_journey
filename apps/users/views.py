from apps.users.models import User
from apps.users.serializer import UserSerializer
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CreateUserPermission(permissions.BasePermission):
    """
    Permission globale personnalisée pour permettre la création d'utilisateurs sans authentification.
    """

    def has_permission(self, request, view):
        # Autoriser l'action de création pour tout le monde
        if view.action == "create":
            return True
        # Pour les autres actions, vérifier l'authentification
        return request.user.is_authenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instance et retourne la liste des permissions que cette vue requiert.
        """
        if self.action == "create":
            permission_classes = [
                CreateUserPermission,
            ]
        else:
            permission_classes = [
                permissions.IsAuthenticated,
            ]
        return [permission() for permission in permission_classes]


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Récupère les informations de l'utilisateur actuellement connecté.
        """
        try:
            user = request.user
            serializer = UserSerializer(user, context={"request": request})
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"erreur": "Utilisateur non trouvé."}, status=404)

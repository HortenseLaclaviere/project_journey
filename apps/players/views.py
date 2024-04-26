from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Player
from .serializer import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"erreur": "Vous devez être connecté.e pour commencer à jouer."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        player, created = Player.objects.get_or_create(user=request.user)

        if created:
            player.save()
            return Response(
                {"message": "Partie créée avec succès."}, status=status.HTTP_201_CREATED
            )

        serializer = self.get_serializer(player)
        return Response(serializer.data)

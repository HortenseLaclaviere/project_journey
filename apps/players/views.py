from apps.players.models import Player
from rest_framework import viewsets
from apps.players.serializer import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

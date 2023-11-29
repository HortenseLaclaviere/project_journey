from apps.choices.models import Choice
from rest_framework import viewsets
from apps.choices.serializer import ChoiceSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

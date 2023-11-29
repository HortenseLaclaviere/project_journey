from apps.stories.models import Story
from rest_framework import viewsets
from apps.stories.serializer import StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

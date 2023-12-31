from .models import Story
from rest_framework import serializers


class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = "__all__"

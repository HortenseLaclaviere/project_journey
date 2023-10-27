from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers

from .models import Story


class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ["story_text", "choices_available", "pk"]


class UserRegistrationSerializer(serializers.Serializer):
    nickname = serializers.CharField(max_length=50)
    mail = serializers.EmailField()
    password = serializers.CharField(write_only=True)  # Le mot de passe ne sera pas inclus dans les réponses


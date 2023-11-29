from .models import Choice
from rest_framework import serializers


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"

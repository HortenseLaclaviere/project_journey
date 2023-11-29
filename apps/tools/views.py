from apps.tools.models import Tool
from rest_framework import viewsets
from apps.tools.serializer import ToolSerializer


class ToolViewSet(viewsets.ModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer

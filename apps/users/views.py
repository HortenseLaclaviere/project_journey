from apps.users.models import User
from rest_framework import viewsets

from apps.users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

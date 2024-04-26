from django.urls import path, include
from rest_framework import routers
from apps.players.views import PlayerViewSet

router = routers.DefaultRouter()

router.register(r"", PlayerViewSet, basename="player")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="player_rest_framework")
    ),
]

from django.urls import path, include
from rest_framework import routers
from apps.stories.views import StoryViewSet

router = routers.DefaultRouter()

router.register(r"story", StoryViewSet, basename="story")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="story_rest_framework")),
]

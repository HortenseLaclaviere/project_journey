from django.urls import path, include
from rest_framework import routers
from apps.choices.views import ChoiceViewSet

router = routers.DefaultRouter()
router.register(r"choices", ChoiceViewSet, basename="choice")

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="choice_rest_framework")
    ),
]

from django.urls import path, include
from rest_framework import routers
from apps.tools.views import ToolViewSet

router = routers.DefaultRouter()

router.register(r"tool", ToolViewSet, basename="tool")

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="tool_rest_framework")),
]

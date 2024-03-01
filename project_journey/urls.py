from django.urls import include, path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("choices/", include("apps.choices.urls")),
    path("players/", include("apps.players.urls")),
    path("story/", include("apps.stories.urls")),
    path("tool/", include("apps.tools.urls")),
    path("bo_pj/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]

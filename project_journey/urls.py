from django.urls import include, path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/users/", include("apps.users.urls")),
    path("api/choices/", include("apps.choices.urls")),
    path("api/players/", include("apps.players.urls")),
    path("api/story/", include("apps.stories.urls")),
    path("api/tool/", include("apps.tools.urls")),
    path("bo_pj/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
]

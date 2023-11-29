from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("choices/", include("apps.choices.urls")),
    path("players/", include("apps.players.urls")),
    path("bo_pj/", admin.site.urls),
]

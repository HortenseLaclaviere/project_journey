from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path("users/", include("apps.users.urls")),
    path("bo_pj/", admin.site.urls),
]

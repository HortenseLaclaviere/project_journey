from django.urls import include, path
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.story_test import views
from apps.story_test.views import UserRegistrationView

urlpatterns = [
    path("bo_pj/", admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("api/", include("apps.story_test.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register", UserRegistrationView.as_view(), name="register"),
]

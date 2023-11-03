from django.urls import path, include
from rest_framework import routers

from . import views
from apps.users.viewset import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
# Create an instance of a router (in this case, a DefaultRouter).
router = routers.DefaultRouter()
# Register the UserViewSet with the router
# to define URLs associated with CRUD operations on users.
router.register(r"users", UserViewSet)

urlpatterns = [
    # Wire up our API using automatic URL routing.
    path("api/", include(router.urls)),
    # Configure the URL to access the authentication features of the API.
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

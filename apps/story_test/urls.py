from django.urls import path
from rest_framework import routers
from . import views
from .views import StoryViewSet

router = routers.DefaultRouter()

router.register('storys', StoryViewSet, basename='storys')

urlpatterns = router.urls

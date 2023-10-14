
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('apps.story_test.urls')),
    path('bo_pj/', admin.site.urls),
]


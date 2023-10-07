
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('apps.urls')),
    path('admin/', admin.site.urls),
]


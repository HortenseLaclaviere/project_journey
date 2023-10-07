
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('game.urls')),
    path('admin/', admin.site.urls),
]


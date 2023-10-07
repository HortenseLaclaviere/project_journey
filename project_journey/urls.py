
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('apps.admin_panel.urls')),
    path('bo_pj/', admin.site.urls),
]


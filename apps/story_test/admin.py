from django.contrib import admin

from.models import Story, Choice

admin.site.register(Story)
# fais apparaitre Story dans l'interface admin

admin.site.register(Choice)


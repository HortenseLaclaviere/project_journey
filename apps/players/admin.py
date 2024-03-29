from django.contrib import admin

from apps.players.models import Player


class PlayerAdmin(admin.ModelAdmin):
    model = Player
    list_display = ("pk", "user", "pseudo")

    def pseudo(self, obj):
        return obj.user.username


admin.site.register(Player, PlayerAdmin)

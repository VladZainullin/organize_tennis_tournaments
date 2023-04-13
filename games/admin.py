from django.contrib import admin

from .models import *


class PlayerAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in Player._meta.get_fields() if f.name != 'id']


admin.site.register(Player, PlayerAdmin)


class GameAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in Game._meta.get_fields() if f.name != 'id']


admin.site.register(Game, GameAdmin)


class GamePlayerAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in GamePlayer._meta.get_fields() if f.name != 'id']


admin.site.register(GamePlayer)

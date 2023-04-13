from django.contrib import admin

from .models import *


class RefereeAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in Referee._meta.get_fields() if f.name != 'id']


admin.site.register(Referee, RefereeAdmin)


class TournamentRefereeAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in TournamentReferee._meta.get_fields() if f.name != 'id']


admin.site.register(TournamentReferee, TournamentRefereeAdmin)
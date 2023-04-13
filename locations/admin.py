from django.contrib import admin

from .models import *

class LocationAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in Location._meta.get_fields() if f.name != 'id']


admin.site.register(Location, LocationAdmin)


class LocationTournamentAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in LocationTournament._meta.get_fields() if f.name != 'id']


admin.site.register(LocationTournament, LocationTournamentAdmin)

from django.contrib import admin

from .models import *


class TournamentsConfig(admin.ModelAdmin):
    list_filter = [f.name for f in Tournament._meta.get_fields() if f.name != 'id']


admin.site.register(Tournament, TournamentsConfig)

from django.contrib import admin

from .models import *

class OrganizerAdmin(admin.ModelAdmin):
    list_filter = [f.name for f in Organizer._meta.get_fields() if f.name != 'id']


admin.site.register(Organizer, OrganizerAdmin)
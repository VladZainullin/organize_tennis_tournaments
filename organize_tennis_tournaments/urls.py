from django.contrib import admin
from django.urls import path, include

from organize_tennis_tournaments.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),

    path('', include('organizers.urls'))
]

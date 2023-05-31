from django.contrib import admin
from django.urls import path
from organize_tennis_tournaments.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home_view, name='home'),
]

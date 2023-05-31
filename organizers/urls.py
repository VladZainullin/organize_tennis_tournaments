from django.urls import path

from organizers.views import *

urlpatterns = [
    path('register-organizer/', register_organizer, name='register_organizer')
]
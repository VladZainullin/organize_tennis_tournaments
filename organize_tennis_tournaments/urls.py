from django.contrib import admin
from django.urls import path, include

from organize_tennis_tournaments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]

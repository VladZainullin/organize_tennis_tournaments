from django.db import models

from games.models import Player
from organizers.models import Organizer


class Tournament(models.Model):
    id: int = models.IntegerField(primary_key=True)
    title: str = models.CharField(max_length=50)
    date_start_registration = models.DateField()
    date_end_registration = models.DateField()
    date_start_tournament = models.DateTimeField()
    date_end_tournament = models.DateTimeField()
    organizer: Organizer = models.ForeignKey(
        to=Organizer,
        on_delete=models.CASCADE)


class Location(models.Model):
    id: int = models.IntegerField(primary_key=True),
    title: str = models.CharField(max_length=50)


class LocationTournament(models.Model):
    id: int = models.IntegerField(primary_key=True),
    location: Location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE)
    tournament: Tournament = models.ForeignKey(
        to=Tournament,
        on_delete=models.CASCADE)
from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True),
    title = models.CharField(max_length=50)

    class Meta:
        db_table = 'location'


class LocationTournament(models.Model):
    id = models.IntegerField(primary_key=True),
    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE)
    tournament = models.ForeignKey(
        to='tournaments.Tournament',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'location_tournament'

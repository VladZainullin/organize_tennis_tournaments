from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True),
    title = models.CharField(max_length=50)

    class Meta:
        db_table = 'locations'
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class LocationTournament(models.Model):
    id = models.IntegerField(primary_key=True),
    location = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE)
    tournament = models.ForeignKey(
        to='tournaments.Tournament',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'location_tournaments'
        verbose_name = 'Место проведения турнира'
        verbose_name_plural = 'Места проведения турниров'

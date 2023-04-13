from django.db import models


class Location(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор'),
    title = models.CharField(
        max_length=50,
        verbose_name='Наименование')

    class Meta:
        db_table = 'locations'
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class LocationTournament(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор'),
    location = models.ForeignKey(
        to=Location,
        verbose_name='Место проведения',
        on_delete=models.CASCADE)
    tournament = models.ForeignKey(
        to='tournaments.Tournament',
        verbose_name='Турнир',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'location_tournaments'
        verbose_name = 'Место проведения турнира'
        verbose_name_plural = 'Места проведения турниров'

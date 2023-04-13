from django.db import models

from tournaments.models import Tournament


class Referee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)

    class Meta:
        db_table = 'referees'
        verbose_name = 'Судья'
        verbose_name_plural = 'Судьи'


class TournamentReferee(models.Model):
    id = models.IntegerField(primary_key=True)
    referee = models.ForeignKey(
        to='referees.Referee',
        on_delete=models.CASCADE)
    tournament = models.ForeignKey(
        to='tournaments.Tournament',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'tournament_referees'
        verbose_name = 'Судья турнира'
        verbose_name_plural = 'Судьи турниров'

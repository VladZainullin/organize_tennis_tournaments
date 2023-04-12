from django.db import models

from tournaments.models import Tournament


class Referee(models.Model):
    id: int = models.IntegerField(primary_key=True)
    name: str = models.CharField(max_length=50)
    surname: str = models.CharField(max_length=50)
    patronymic: str = models.CharField(max_length=50)


class TournamentReferee(models.Model):
    id: int = models.IntegerField(primary_key=True)
    referee: Referee = models.ForeignKey(
        Referee,
        on_delete=models.CASCADE)
    tournament: Tournament = models.ForeignKey(
        to=Tournament,
        on_delete=models.CASCADE)

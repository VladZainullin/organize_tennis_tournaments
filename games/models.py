from django.db import models


class Game(models.Model):
    id: int = models.IntegerField(primary_key=True)
    winner_player: Player = models.ForeignKey(
        to=Player,
        on_delete=models.CASCADE,
        null=True)
    tournament_referee: TournamentReferee = models.ForeignKey(
        to=TournamentReferee,
        on_delete=models.CASCADE)


class Player(models.Model):
    id: int = models.IntegerField(primary_key=True)
    name: str = models.CharField(max_length=50)
    surname: str = models.CharField(max_length=50)
    patronymic: str = models.CharField(max_length=50)
    tournament: Tournament = models.ForeignKey(
        to=Tournament,
        on_delete=models.CASCADE)


class GamePlayer(models.Model):
    id: int = models.IntegerField(primary_key=True)
    player: Player = models.ForeignKey(
        to=Player,
        on_delete=models.CASCADE)
    game: Game = models.ForeignKey(
        to=Game,
        on_delete=models.CASCADE)
from django.db import models

from tournaments.models import Tournament
from referees.models import TournamentReferee


class Player(models.Model):
    id: int = models.IntegerField(primary_key=True)
    name: str = models.CharField(max_length=50)
    surname: str = models.CharField(max_length=50)
    patronymic: str = models.CharField(max_length=50)
    tournament = models.ForeignKey(
        to='tournaments.Tournament',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'players'
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Game(models.Model):
    id: int = models.IntegerField(primary_key=True)
    winner_player: Player = models.ForeignKey(
        to=Player,
        on_delete=models.CASCADE,
        null=True)
    tournament_referee: TournamentReferee = models.ForeignKey(
        to=TournamentReferee,
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'games'
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'


class GamePlayer(models.Model):
    id: int = models.IntegerField(primary_key=True)
    player: Player = models.ForeignKey(
        to=Player,
        on_delete=models.CASCADE)
    game: Game = models.ForeignKey(
        to=Game,
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'game_players'
        verbose_name = 'Партия игроков'
        verbose_name_plural = 'Партии игроков'

from django.db import models

from tournaments.models import Tournament
from referees.models import TournamentReferee


class Player(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    name: str = models.CharField(
        max_length=50,
        verbose_name='Имя')
    surname: str = models.CharField(
        max_length=50,
        verbose_name='Фамилия')
    patronymic: str = models.CharField(
        max_length=50,
        verbose_name='Отчество',
        null=True)
    tournament = models.ForeignKey(
        to='tournaments.Tournament',
        verbose_name='Турнир',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'players'
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Game(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    winner_player: Player = models.ForeignKey(
        to=Player,
        verbose_name='Победитель партии',
        on_delete=models.CASCADE,
        null=True)
    tournament_referee: TournamentReferee = models.ForeignKey(
        to=TournamentReferee,
        verbose_name='Судья партии',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'games'
        verbose_name = 'Партия'
        verbose_name_plural = 'Партии'


class GamePlayer(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    player: Player = models.ForeignKey(
        to=Player,
        verbose_name='Игрок',
        on_delete=models.CASCADE)
    game: Game = models.ForeignKey(
        to=Game,
        verbose_name='Игра',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'game_players'
        verbose_name = 'Партия игроков'
        verbose_name_plural = 'Партии игроков'

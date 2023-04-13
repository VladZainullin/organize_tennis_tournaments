from django.db import models

from tournaments.models import Tournament


class Referee(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    name = models.CharField(
        max_length=50,
        verbose_name='Имя')
    surname = models.CharField(
        max_length=50,
        verbose_name='Фамилия')
    patronymic = models.CharField(
        max_length=50,
        verbose_name='Отчество')

    class Meta:
        db_table = 'referees'
        verbose_name = 'Судья'
        verbose_name_plural = 'Судьи'


class TournamentReferee(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    referee = models.ForeignKey(
        to='referees.Referee',
        verbose_name='Судья',
        on_delete=models.CASCADE)
    tournament = models.ForeignKey(
        to='tournaments.Tournament',
        verbose_name='Турнир',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'tournament_referees'
        verbose_name = 'Судья турнира'
        verbose_name_plural = 'Судьи турниров'

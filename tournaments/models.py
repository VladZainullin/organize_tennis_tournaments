from django.db import models


class Tournament(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    title = models.CharField(
        max_length=50,
        verbose_name='Наименование')
    description = models.CharField(
        max_length=5000,
        verbose_name='Описание')
    date_start_registration = models.DateField(
        verbose_name='Дата начала регистрации')
    date_end_registration = models.DateField(
        verbose_name='Дата окончания регистрации')
    date_start_tournament = models.DateTimeField(
        verbose_name='Дата начала турнира')
    date_end_tournament = models.DateTimeField(
        verbose_name='Дата окончания турнира')
    organizer = models.ForeignKey(
        to='organizers.Organizer',
        verbose_name='Организатор',
        on_delete=models.CASCADE),
    image = models.ImageField(upload_to='tournaments/images/%Y/%m/%d')

    class Meta:
        db_table = 'tournaments'
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'


class TournamentPlayer(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    tournament = models.ForeignKey(
        to=Tournament,
        verbose_name='Турнир',
        on_delete=models.CASCADE)
    player = models.ForeignKey(
        to='games.Player',
        verbose_name='Игрок',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'tournament_players'
        verbose_name = 'Участник турнира'
        verbose_name_plural = 'Участники турнира'

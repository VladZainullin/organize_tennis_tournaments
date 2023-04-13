from django.db import models

from organizers.models import Organizer


class Tournament(models.Model):
    id: int = models.IntegerField(
        primary_key=True,
        verbose_name='Идентификатор')
    title = models.CharField(
        max_length=50,
        verbose_name='Наименование')
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
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'tournaments'
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'

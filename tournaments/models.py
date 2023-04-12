from django.db import models

from organizers.models import Organizer


class Tournament(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    date_start_registration = models.DateField()
    date_end_registration = models.DateField()
    date_start_tournament = models.DateTimeField()
    date_end_tournament = models.DateTimeField()
    organizer = models.ForeignKey(
        to='organizers.Organizer',
        on_delete=models.CASCADE)
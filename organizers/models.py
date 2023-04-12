from django.db import models


class Organizer(models.Model):
    id: int = models.IntegerField(primary_key=True)
    title: int = models.CharField(max_length=50)

    class Meta:
        db_table = 'organizer'

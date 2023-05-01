from django.db import models
from django.contrib.auth.models import User


class Organizer(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Наименование')
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'organizers'
        verbose_name = 'Организатор'
        verbose_name_plural = 'Организаторы'

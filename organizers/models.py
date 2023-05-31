from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models


class Organizer(models.Model):
    title = models.CharField(max_length=50)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

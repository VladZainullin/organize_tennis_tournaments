from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Organizer(AbstractUser):
    title = models.CharField(max_length=50)

    groups = models.ManyToManyField(Group, related_name='organizers')
    user_permissions = models.ManyToManyField(Permission, related_name='organizers')

    def __str__(self):
        return self.username

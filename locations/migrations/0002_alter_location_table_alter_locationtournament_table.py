# Generated by Django 4.2 on 2023-04-13 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='location',
            table='locations',
        ),
        migrations.AlterModelTable(
            name='locationtournament',
            table='location_tournaments',
        ),
    ]

# Generated by Django 4.2 on 2023-05-01 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_tournament_description_alter_tournament_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TournamentPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament', verbose_name='Турнир')),
            ],
            options={
                'verbose_name': 'Участник турнира',
                'verbose_name_plural': 'Участники турнира',
                'db_table': 'tournament_players',
            },
        ),
    ]

# Generated by Django 4.2 on 2023-05-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'Партия',
                'verbose_name_plural': 'Партии',
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'Партия игроков',
                'verbose_name_plural': 'Партии игроков',
                'db_table': 'game_players',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Идентификатор')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=50, null=True, verbose_name='Отчество')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
                'db_table': 'players',
            },
        ),
    ]

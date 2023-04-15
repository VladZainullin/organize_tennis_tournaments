# Generated by Django 4.2 on 2023-04-15 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_remove_tournament_organizer_tournament_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='description',
            field=models.CharField(default='', max_length=5000, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='image',
            field=models.ImageField(upload_to='tournaments/images/%Y/%m/%d'),
        ),
    ]

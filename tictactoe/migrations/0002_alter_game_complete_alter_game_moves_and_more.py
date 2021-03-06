# Generated by Django 4.0.3 on 2022-05-09 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='moves',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_one',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_two',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.IntegerField(null=True),
        ),
    ]

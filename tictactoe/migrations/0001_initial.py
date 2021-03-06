# Generated by Django 4.0.3 on 2022-05-09 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_one', models.IntegerField()),
                ('player_two', models.IntegerField()),
                ('moves', models.TextField()),
                ('complete', models.BooleanField()),
                ('winner', models.IntegerField()),
            ],
        ),
    ]

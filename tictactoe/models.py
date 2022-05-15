from pickle import TRUE
from django.db import models

class Game (models.Model):
    player_one = models.IntegerField(null=True) #user_id
    player_two = models.IntegerField(null=True) #user_id
    moves = models.TextField(null=True) 
    complete = models.BooleanField(default=False) #true is complete
    winner = models.IntegerField(null=True) #user_id, 0 is draw


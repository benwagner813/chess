from django.db import models

# Create your models here.
class Chess (models.Model):
    player_white = models.IntegerField(null=True) #userID
    player_black = models.IntegerField(null=True) #userID
    fen = models.TextField(null=True)
    moves = models.TextField(null=True)
    complete = models.BooleanField(default=False) #true is complete
    winner = models.IntegerField(null=True) #user_id, 0 is draw
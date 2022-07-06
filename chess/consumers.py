import json
import logging
import random
from .models import Chess
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChessConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['id']

        self.group_name = 'game_%s' % self.game_id
        self.user = self.scope['user']
        self.player = ''
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        if (await self.assign_player()):
            await self.accept()
        
        else:
            await self.close()

    @database_sync_to_async
    def assign_player(self):
        game = Chess.objects.get(pk=self.game_id)

        if self.user.is_anonymous or game.complete: #returns false if the game is complete or the user is not logged in (used to deny connections)
            return False

        if (self.user.id == game.player_white or self.user.id == game.player_black):
            if(self.user.id == game.player_white):
                self.player = '1'
            if(self.user.id == game.player_black):
                self.player = '2'
            return True

        if (game.player_white is None and game.player_black is None):
            randNum = random.randint(1, 2)
            if (randNum == 1):
                game.player_white = self.user.id
                self.player = "1"
            else:
                game.player_black = self.user.id
                self.player = "2"
            game.save()
            return True
        
        if (game.player_white is not None and game.player_black is None):
            game.player_black = self.user.id
            game.save()
            self.player = "2"
            return True

        if (game.player_white is None and game.player_black is not None):
            game.player_white = self.user.id
            game.save()
            self.player = "1"
            return True

        return False


class ChessLobbyConsumer(AsyncWebsocketConsumer):
    pass


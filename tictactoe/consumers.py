import json
from textwrap import fill
from .models import Game
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class TTTConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']

        self.group_name = 'game_%s' % self.game_id
        self.user = self.scope['user']

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await database_sync_to_async(self.dbCalls)()
        self.accept()

    def dbCalls(self):
        game = Game.objects.get(pk=self.game_id)

        if (game.player_one == None):
            game.player_one = self.user.id
            game.save()
            
        elif (game.player_two == None):
            game.player_two = self.user.id
            game.save()

    async def disconnect(self, code):
        pass

class TTTLobbyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
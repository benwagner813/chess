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
        self.player = ''
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        if(await database_sync_to_async(self.dbCalls)()): #If dbCalls returns True connect the user
           await self.accept()
           await self.channel_layer.group_send( #send to channel layer
               self.group_name,
               {
                    "type" : "send_user",
                    "user" : self.user.username,
                    "player" : self.player
               }
           )
    
    async def send_user(self, event): # send to websocket
        username = event['user']
        player = event['player']
        await self.send(text_data=json.dumps({
          'username' : username,
          'player' : player
        }))


    def dbCalls(self): #dbCalls checks if the user matches the database and enters the user in the game if there is none
        game = Game.objects.get(pk=self.game_id)

        if (self.user.id == game.player_one or self.user.id == game.player_two):
            if(self.user.id == game.player_one):
                self.player = '1'
            if(self.user.id == game.player_two):
                self.player = '2'
            return True

        elif (game.player_one == None):
            game.player_one = self.user.id
            game.save()
            self.player = '1'
            return True
            
        elif (game.player_two == None):
            game.player_two = self.user.id
            game.save()
            self.player = '2'
            return True

        else:
            return False

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

class TTTLobbyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
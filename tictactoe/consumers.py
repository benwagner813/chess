import json
import logging
from textwrap import fill
from .models import Game
from .Tictactoe import Tictactoe
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class TTTConsumer(AsyncWebsocketConsumer):

    logging.basicConfig(level=logging.INFO)

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
           game = await database_sync_to_async(self.getGame)()
           moves = game.moves
           elp = Tictactoe(moves)

           await self.channel_layer.group_send( #send to channel layer
               self.group_name,
               {
                    "type" : "send_user",
                    "user" : self.user.username,
                    "player" : self.player,
                    "available_move_list": elp.list_moves()
               }
           )

           self.group_player = self.group_name + self.player
           await self.channel_layer.group_add(
               self.group_player,
               self.channel_name
           )

    def getGame(self):
        return Game.objects.get(pk=self.game_id)
    
    async def send_user(self, event): # send to websocket
        username = event['user']
        player = event['player']
        available_move_list = event['available_move_list']
        await self.send(text_data=json.dumps({
          'username' : username,
          'player' : player,
          'available_move_list': available_move_list
        }))

    async def receive(self, text_data):
        if(self.player == '1'):
            player_group = self.group_name + '2'
        else:
            player_group = self.group_name + '1'

        text_data_json = json.loads(text_data)
        move = text_data_json['move']
        moves = await self.add_move_db(move)
        game = Tictactoe(moves)
        if(game.isWin()):
            pass

        available_move_list = game.list_moves()
        logging.info(available_move_list)

        await self.channel_layer.group_send(
            player_group,
            {
                'type' : 'player_move',
                'move' : move,
                'available_move_list' : available_move_list
            }
        )

    async def player_move(self, event):#send the move to player websocket
        move = event['move']
        available_move_list = event['available_move_list']
        logging.info(available_move_list)
        await self.send(text_data=json.dumps({
            'move': move,
            'available_move_list' : available_move_list
        }))
        logging.info("The server sent the move down the websocket")

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

    @database_sync_to_async
    def add_move_db(self, move):
        game = Game.objects.get(pk=self.game_id)
        moves = game.moves
        if(moves == None):
            moves = move
        else:
            moves = moves + ',' + move

        game.moves = moves
        game.save()
        return game.moves

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

class TTTLobbyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
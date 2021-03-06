import json
import logging, time
from tracemalloc import start
from .models import Game
from django.contrib.auth.models import User
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
            tictactoe = Tictactoe(moves)
            if(tictactoe.turn == int(self.player)):
                self.turn = True
            else:
                self.turn = False

            await self.channel_layer.group_send( #send to channel layer
               self.group_name,
               {
                    "type" : "send_user",
                    "user" : self.user.username,
                    "player" : self.player,
                    "available_move_list": tictactoe.list_moves()
               }
            )

            self.group_player = self.group_name + self.player
            await self.channel_layer.group_add(
                self.group_player,
                self.channel_name
            )
            await self.channel_layer.group_send(
                self.group_player,
                {
                    "type" : "send_turn",
                    "turn" : self.turn
                }
            )
        else:
            await self.close()

    
    async def send_user(self, event): # send to websocket
        username = event['user']
        player = event['player']
        available_move_list = event['available_move_list']
        await self.send(text_data=json.dumps({
          'username' : username,
          'player' : player,
          'available_move_list': available_move_list
        }))
    
    async def send_turn(self, event):#if it is the players turn send true else false
        turn = event['turn']
        await self.send(text_data=json.dumps({
            'turn' : turn
        }))

    async def receive(self, text_data):#This method fires every time a message is received from a web socket
        if(self.player == '1'):
            player_group = self.group_name + '2'
        else:
            player_group = self.group_name + '1'

        text_data_json = json.loads(text_data)#Get the move data from JSON and instantiate tictactoe object
        move = text_data_json['move']
        moves = await self.add_move_db(move)
        game = Tictactoe(moves)

        available_move_list = game.list_moves()

        await self.channel_layer.group_send(#Send the move and the resulting available moves to the opponent
            player_group,
            {
                'type' : 'player_move',
                'move' : move,
                'available_move_list' : available_move_list
            }
        )

        if(game.isWin()):#check for game win
            winner = await self.add_win_db()
            winCombo = game.winCombo
            winning_player = (2, 1)[self.player == '1']
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type" : "send_win",
                    "winner" : winner,
                    "winning_player" : winning_player,
                    "winCombo" : winCombo
                }
            )
        elif(len(available_move_list) == 0):#If the game is not won and the available moves is 0 then the game is a draw
            await self.add_draw_db()
            winner = 0
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type" : "send_draw",
                    "winner" : winner
                }
            )

    async def send_draw(self, event):#sends a message with a winner of 0 indicating a draw
        winner = event['winner']
        await self.send(text_data=json.dumps({
            'winner' : winner
        }))

    async def send_win(self, event):#sends a message containing the winners username and the player that won (1 or 2)
        winner = event['winner']
        winning_player = event['winning_player']
        winCombo = event['winCombo']
        await self.send(text_data=json.dumps({
            'winner' : winner,
            'winning_player' : winning_player,
            'winCombo' : winCombo
        }))

    async def player_move(self, event):#send the move to player websocket
        move = event['move']
        available_move_list = event['available_move_list']
        await self.send(text_data=json.dumps({
            'move': move,
            'available_move_list' : available_move_list
        }))
        
    def getGame(self):
        return Game.objects.get(pk=self.game_id)

    def dbCalls(self): #dbCalls checks if the user matches the database and enters the user in the game if there is none
        game = Game.objects.get(pk=self.game_id)
        
        if self.user.is_anonymous or game.complete:#returns false if the game is complete or the user is not logged in (used to deny connections)
            return False
        
        if (self.user.id == game.player_one or self.user.id == game.player_two):
            if(self.user.id == game.player_one):
                self.player = '1'
            if(self.user.id == game.player_two):
                self.player = '2'
            return True

        elif (game.player_one is None):
            game.player_one = self.user.id
            game.save()
            self.player = '1'
            return True
            
        elif (game.player_two is None):
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

    @database_sync_to_async
    def add_win_db(self):
        game = Game.objects.get(pk=self.game_id)
        game.complete = True
        game.winner = (game.player_two, game.player_one)[self.player == '1']
        game.save()
        winner = User.objects.get(pk=game.winner)
        return winner.username

    @database_sync_to_async
    def add_draw_db(self):
        game = Game.objects.get(pk=self.game_id)
        game.complete = True
        game.winner = 0
        game.save()
        

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

class TTTLobbyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
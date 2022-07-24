import json
import logging
import random
import chess
from .models import Chess
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChessConsumer(AsyncWebsocketConsumer):

    logging.basicConfig(level=logging.INFO)

    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['id']

        self.group_name = 'game_%s' % self.game_id
        self.user = self.scope['user']
        self.player = ''
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        if (await self.assign_player()): #Check if player is eligible to connect (as well as database inputs)
            await self.accept()
            await self.channel_layer.group_send( #Send message on connect with the player username to channel layer
               self.group_name,
               {
                    "type" : "player_connect",
                    "user" : self.user.username,
                    "color" : self.player,
               }
            )
            
            self.chess = chess.Board() 
            self.chess.set_epd(self.epd)#initialize the chess game based on the epd in the db

            self.group_player = self.group_name + self.player
            await self.channel_layer.group_add( #add the player to their own group where they will receive move messages from the other player
                self.group_player,
                self.channel_name
            )
        else:
            await self.close()

    async def receive(self, text_data):
        if(self.player == '1'): #The move message needs to be sent to the opposing player
            player_group = self.group_name + '2'
        else:
            player_group = self.group_name + '1'

        text_data_json = json.loads(text_data)
        move = text_data_json['move'] #load move from json
        move = chess.Move.from_uci(move)
        move_san = self.chess.san(move)
        self.chess.push(move) #make the move with the chess object
        moves = await self.add_move_db(move_san) #add the move to the database
        
        available_move_list = []
        for move in self.chess.legal_moves: #add the uci strings of the legal moves to a list
            available_move_list.append(move.uci())
       
        new_avail_moves = {}
        key = available_move_list[0][:2] #key starts off equaling first 2 chars of first value
        for string in available_move_list: #for each item in the original available move list
            if key in string:
                if key in new_avail_moves.keys(): #has key already
                    new_avail_moves[key].append(string[2:])
                else: #doesn't have the key already
                    new_avail_moves[key] = []
                    new_avail_moves[key].append(string[2:])
            else: #no longer any more of this key
                key = string[:2]
                new_avail_moves[key] = []
                new_avail_moves[key].append(string[2:])
        
        await self.channel_layer.group_send(
            player_group,
            {
                'type' : 'player_move',
                'move' : text_data_json['move'],
                'available_move_list' : new_avail_moves
            }
        )

    async def player_connect(self, event): #Send message from channel layer to websocket
        username = event['user']
        color = event['color']
        await self.send(text_data=json.dumps({
            'username' : username,
            'color' : color,
        }))
    
    async def player_move(self, event):#send the move to player websocket
        move = event['move']
        available_move_list = event['available_move_list']
        await self.send(text_data=json.dumps({
            'move': move,
            'available_move_list' : available_move_list
        }))

    @database_sync_to_async
    def assign_player(self):
        game = Chess.objects.get(pk=self.game_id)
        self.epd = game.epd
        logging.info(self.epd)
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

    @database_sync_to_async
    def add_move_db(self, move_san):
        game = Chess.objects.get(pk=self.game_id)
        if(self.chess.turn):
            move = f"{move_san} "
        else:
            move = f"{self.chess.fullmove_number}. {move_san} "
        game.moves = game.moves + move if game.moves is not None else move
        game.epd = self.chess.epd(hmvc=self.chess.halfmove_clock, fmvn=self.chess.fullmove_number)
        game.save()
        return game.moves

class ChessLobbyConsumer(AsyncWebsocketConsumer):
    pass


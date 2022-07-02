import json
import logging
from .models import Game
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChessConsumer(AsyncWebsocketConsumer):
    pass

class ChessLobbyConsumer(AsyncWebsocketConsumer):
    pass


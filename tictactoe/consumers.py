import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TTTConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']

        self.group_name = 'game_%s' % self.game_id
        self.user = self.scope['user']

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        pass

class TTTLobbyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
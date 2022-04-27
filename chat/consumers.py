import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.channel_layer.group_send(
            "Lobby",
            {
                'type': 'room_create',
                'name': self.room_name
            }
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_send(
            "Lobby",
            {
                'type': 'room_delete',
                'name': self.room_name
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.user.username
        group_name = self.room_group_name

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'group_name': group_name
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        group_name = event['group_name']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'group_name': group_name
        }))

class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "Lobby",
            self.channel_name
        )
        self.room_list = {}
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            "Lobby",
            self.channel_name
        )

    async def room_create(self, event):
        room = event['name']
        if room in self.room_list.keys():
            self.room_list[room] += 1
        else:
            self.room_list[room] = 1
        
        await self.send(text_data=json.dumps({
            'list': self.room_list
        }))
    
    async def room_delete(self, event):
        room = event['name']
        if room in self.room_list.keys():
            if self.room_list[room] > 1:
                self.room_list[room] -= 1
            elif self.room_list[room] == 1:
                self.room_list.pop(room)
        
        await self.send(text_data=json.dumps({
            'list': self.room_list
        }))
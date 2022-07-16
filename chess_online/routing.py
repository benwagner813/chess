from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chess/(?P<id>\w+)/$', consumers.ChessConsumer.as_asgi()),
    re_path(r'ws/chess/lobby', consumers.ChessLobbyConsumer.as_asgi()),
]
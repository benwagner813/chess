from django.urls import path

from . import views

app_name = 'tictactoe'

urlpatterns = [
    path('lobby/', views.tttLobby, name="TicTacToeLobby"),
    path('<int:game_id>/', views.tttGame, name="TicTacToeGame"),
    path('createGame/', views.createGame, name="createGame")
]

from django.urls import path

from . import views

app_name = 'chess'

urlpatterns = [
    path('lobby/', views.chessLobby, name="ChessLobby"),
    path('<int:id>/', views.chessGame, name="ChessGame"),
    path('createGame/', views.createGame, name="createGame")
]

from django.shortcuts import render, redirect
from .models import Chess
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.models import User
import chess

def chessLobby(request):
    return render(request, "chess/chessLobby.html", {})

def chessGame(request, id):
    try:
        game = Chess.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    
    white_UN = 'Waiting for player...'
    black_UN = 'Waiting for player...'
    
    if (User.objects.filter(id=game.player_white).exists()):
        player_one = User.objects.get(pk=game.player_white)
        white_UN = player_one.username
    if (User.objects.filter(id=game.player_black).exists()):
        player_two = User.objects.get(pk=game.player_black)
        black_UN = player_two.username

    return render(request, "chess/chess.html", {
        'id' : id,
        'white' : white_UN,
        'black' : black_UN,
    })

def createGame(request):
    game = Chess()
    game.epd = chess.Board().epd()
    game.save()
    return redirect("chess_online:ChessGame", id = game.id)
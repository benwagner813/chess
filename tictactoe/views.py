from django.shortcuts import render, redirect
from django.http import Http404
from tictactoe.Tictactoe import Tictactoe
from .models import Game
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import logging


def tttLobby(request):
    return render(request, "tictactoe/tttLobby.html", {})

def tttGame(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except ObjectDoesNotExist:
        raise Http404

    if (game.moves == None):
        tictactoe = Tictactoe("")
    else:
        tictactoe = Tictactoe(game.moves)
    available_move_list = tictactoe.list_moves()
    
    winCombo = ""
    if game.winner == 0:
        winnerUN = 0
    elif game.winner is not None:
        winner = User.objects.get(pk=game.winner)
        winnerUN = winner.username
        tictactoe.isWin()
        winCombo = tictactoe.winCombo
    else:
        winnerUN = None

    player_one_UN = 'Waiting for player...'
    player_two_UN = 'Waiting for player...'

    if (User.objects.filter(id=game.player_one).exists()):
        player_one = User.objects.get(pk=game.player_one)
        player_one_UN = player_one.username
    if (User.objects.filter(id=game.player_two).exists()):
        player_two = User.objects.get(pk=game.player_two)
        player_two_UN = player_two.username

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    return render(request, "tictactoe/tictactoe.html", 
        {
            'game_id' : game_id,
            'player_one_UN': player_one_UN,
            'player_two_UN': player_two_UN,
            'available_move_list': available_move_list,
            'moves': game.moves,
            'username': username,
            'winnerUN' : winnerUN,
            'winCombo' : winCombo
        })

def createGame(request):
    game = Game()
    game.save()
    logging.basicConfig(level=logging.CRITICAL)
    logging.debug(game.player_one)
    return redirect("tictactoe:TicTacToeGame", game_id = game.id)
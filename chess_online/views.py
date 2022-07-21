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
    chessBoard = chess.Board()
    chessBoard.set_epd(game.epd)
    available_move_list = []
    for move in chessBoard.legal_moves: #add the uci strings of the legal moves to a list
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
        'epd' : game.epd,
        'available_moves' : new_avail_moves,
    })

def createGame(request):
    game = Chess()
    game.epd = chess.Board().epd()
    game.save()
    return redirect("chess_online:ChessGame", id = game.id)
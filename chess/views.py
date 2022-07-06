from django.shortcuts import render, redirect
from .models import Chess


def chessLobby(request):
    return render(request, "chess/chessLobby.html", {})

def chessGame(request, id):
    return render(request, "chess/chess.html", {
        'id' : id,
    })

def createGame(request):
    game = Chess()
    game.save()
    return redirect("chess:ChessGame", id = game.id)
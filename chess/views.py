from django.shortcuts import render


def chessLobby(request):
    return render(request, "chess/chessLobby.html", {})

def chessGame(request, id):
    return render(request, "chess/chess.html", {})

def createGame(request):
    pass

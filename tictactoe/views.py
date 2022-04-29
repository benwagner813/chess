from django.shortcuts import render

def tttLobby(request):
    return render(request, "tictactoe/tttLobby.html", {})

def tttGame(request, game_id):
    return render(request, "tictactoe/tictactoe.html", {'game_id' : game_id})

class tictactoe:

    def __init__(self, playerX, playerO):
        self.playerX = playerX
        self.playerO = playerO
        self.grid = [
            [0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0]
        ]

    def move(self, r, c, player):
        self.grid[r][c] = player

    def isWin(self):
        grid = self.grid
        for i in range(3):
            if(grid[i][0] == grid[i][1] and grid[i][0] != 0):
                if(grid[i][1] == grid[i][2]):
                    return True
            if(grid[0][i] == grid[1][i] and grid[0][i] != 0):
                if(grid[1][i] == grid[2][i]):
                    return True
        if(grid[0][0] == grid[1][1] and grid[0][0] != 0):
            if(grid[1][1] == grid[2][2]):
                return True
        if(grid[2][0] == grid[1][1] and grid[2][0] != 0):
            if(grid[1][1] == grid[0][2]):
                return True
        return False

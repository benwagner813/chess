class Tictactoe:

    #blank is 0, o is 1, x is 2
    def __init__(self, moves):
        self.playerX = 2
        self.playerO = 1
        self.moves = moves
        self.grid = [
            [0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.turn = 1
        self.create_board_state(self.moves)

    def move(self, r, c, player):
        self.grid[r][c] = player
        return self.grid

    def isWin(self):
        grid = self.grid
        for i in range(3):
            # checks if horizontal win
            if(grid[i][0] == grid[i][1] and grid[i][0] != 0):
                if(grid[i][1] == grid[i][2]):
                    self.winCombo = f"row-{i+1}"
                    return True
            # checks if vertical win
            if(grid[0][i] == grid[1][i] and grid[0][i] != 0):
                if(grid[1][i] == grid[2][i]):
                    self.winCombo = f"col-{i+1}"
                    return True
        # checks if diagonal win
        if(grid[0][0] == grid[1][1] and grid[0][0] != 0):
            if(grid[1][1] == grid[2][2]):
                self.winCombo = "dia-dright"
                return True
        if(grid[2][0] == grid[1][1] and grid[2][0] != 0):
            if(grid[1][1] == grid[0][2]):
                self.winCombo = "dia-dleft"
                return True
        return False

    #creates the board state based on the string of moves the game is initialized with
    def create_board_state(self, moves):
        if(moves == None or len(moves) == 0):
            return
        moves_list = moves.split(',')
        for count, move in enumerate(moves_list):
            c = int(move[1])
            r = int(move[0])    
            if(count%2 == 0):
                self.grid[r][c] = 1
            else:
                self.grid[r][c] = 2
        self.turn = 1 if len(moves_list) % 2 == 0 else 2

    # lists available moves
    def list_moves(self):
        move_list = []
        for r in range(3):
            for c in range(3):
                if(self.grid[r][c] == 0):
                    move_list.append(str(r) + str(c))
        return move_list
    

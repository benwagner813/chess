class Chess:

    def __init__(self) -> None:
        self.board = [
            ["R","N","B","Q","K","B","N","R"],
            ["P","P","P","P","P","P","P","P"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["_","_","_","_","_","_","_","_"],
            ["p","p","p","p","p","p","p","p"],
            ["r","n","b","q","k","b","n","r"]
        ]
        self.turn = "White"

    def is_win() -> bool:
        pass

    def is_draw() -> bool:
        pass
    
    def is_check() -> bool:
        pass

    def available_moves() -> list:
        pass
    
    def move(self, startPos:str, endPos:str):
        startCol = ord(startPos[0]) - 65
        startRow = int(startPos[1]) - 1

        endCol = ord(endPos[0]) - 65
        endRow = int(endPos[1]) - 1

        piece = self.board[startRow][startCol]
        print(piece)

        # print(self.board[endRow][endCol])

        if (endCol in range(8) and endRow in range(8)): #if the endPos is in the bounds of the board

            if (piece == "P" or piece == "p"): #move pawn
                self.mPawn(piece, startRow, startCol, endRow, endCol)

            elif (piece == "N" or piece == "n"): #move knight
                self.mKnight(piece, startRow, startCol, endRow, endCol)
            
            elif (piece == "K" or piece == "k"): #move king
                self.mKing(piece, startRow, startCol, endRow, endCol)

            elif (piece == "B" or piece == "b"): #move bishop
                self.mBishop(piece, startRow, startCol, endRow, endCol)
        
         
    # move pawn function
    def mPawn(self, piece, startRow, startCol, endRow, endCol):
        if (piece == "P"): #if the piece is a White pawn
            if (endCol == startCol): #if endCol is same, it is trying to move

                if (self.board[endRow][endCol] == "_"): #the end pos is valid so it is valid

                    if(startRow == 1): #if the pawn is on starting pos it can move two squares
                        if(endRow == startRow + 2 and self.board[startRow + 1][startCol] == "_"): #if moving 2 square, check first square is clear
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "P"
                            self.swap() #switch who's turn it is
                        elif(endRow == startRow + 1):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "P"           
                            self.swap() #switch who's turn it is   

                    else: #else it can only move one square
                        if(endRow == startRow + 1):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "P"
                            self.swap() #switch who's turn it is 
            
            elif (endCol == startCol + 1 or endCol == startCol - 1): #if endCol is to side, it is trying to capture
                
                if (endRow == startRow + 1 and self.board[endRow][endCol].islower()): #if it is one row ahead and it is a Black piece
                    self.board[startRow][startCol] = "_"
                    self.board[endRow][endCol] = "P"           
                    self.swap() #switch who's turn it is

        elif (piece == "p"): #if the piece is a Black pawn
            if (endCol == startCol):

                if (self.board[endRow][endCol] == "_"): #the end pos is valid so it is valid

                    if(startRow == 6): #if the pawn is on starting pos it can move two squares
                        if(endRow == startRow - 2 and self.board[startRow - 1][startCol] == "_"): #if moving 2 square, check first square is clear
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "p"
                            self.swap() #switch who's turn it is
                        elif(endRow == startRow - 1): 
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "p"
                            self.swap() #switch who's turn it is

                    else: #else it can only move one square
                        if(endRow == startRow - 1):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "p"
                            self.swap() #switch who's turn it is
            
            elif (endCol == startCol + 1 or endCol == startCol - 1): #if endCol is to side, it is trying to capture
                
                if (endRow == startRow - 1 and self.board[endRow][endCol].isupper()): #if it is one row ahead and it is a White piece
                    self.board[startRow][startCol] = "_"
                    self.board[endRow][endCol] = "p"           
                    self.swap() #switch who's turn it is

    # move knight function
    def mKnight(self, piece, startRow, startCol, endRow, endCol):
        if (endCol == startCol + 1 or endCol == startCol - 1): 
            if (endRow == startRow + 2 or endRow == startRow - 2): #if end pos is up 2 over 1

                if (piece == "N"): #if it is a White knight
                    if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
                        self.board[startRow][startCol] = "_"
                        self.board[endRow][endCol] = "N"           
                        self.swap() #switch who's turn it is

                else: #else its a Black knight
                    if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
                        self.board[startRow][startCol] = "_"
                        self.board[endRow][endCol] = "n"           
                        self.swap() #switch who's turn it is

        elif (endCol == startCol + 2 or endCol == startCol - 2):
            if (endRow == startRow + 1 or endRow == startRow - 1): #if end pos is up 1 over 2

                if (piece == "N"): #if it is a White knight
                    if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
                        self.board[startRow][startCol] = "_"
                        self.board[endRow][endCol] = "N"           
                        self.swap() #switch who's turn it is

                else: #else its a Black knight
                    if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
                        self.board[startRow][startCol] = "_"
                        self.board[endRow][endCol] = "n"           
                        self.swap() #switch who's turn it is

    # move king function
    def mKing(self, piece, startRow, startCol, endRow, endCol):
        if (startCol - 1 <= endCol <= startCol + 1 and startRow - 1 <= endRow <= startRow + 1): #if end pos is within 1 of start pos
            
            if (piece == "K"): #if it is a White king
                if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
                    self.board[startRow][startCol] = "_"
                    self.board[endRow][endCol] = "K"           
                    self.swap() #switch who's turn it is

            else: #else it's a Black king
                if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
                    self.board[startRow][startCol] = "_"
                    self.board[endRow][endCol] = "k"           
                    self.swap() #switch who's turn it is

    # move bishop function
    def mBishop(self, piece, startRow, startCol, endRow, endCol):
        if (abs(endCol - startCol) == abs(endRow - startRow)): #if moving diagonally
            
            if (endCol - startCol > 0): #if moving to right
                
                if (endRow - startRow > 0): #if moving up (according to Ben)
                    for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
                        if (self.board[startRow + i][startCol + i] != "_"): #checking if the square is empty
                            return False

                    if (piece == "B"): #if it is a White bishop
                        if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "B"           
                            self.swap() #switch who's turn it is

                    else: #else it's a Black bishop
                        if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "b"           
                            self.swap() #switch who's turn it is

                else: #else it is moving down
                    for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
                        if (self.board[startRow - i][startCol + i] != "_"): #checking if the square is empty
                            return False

                    if (piece == "B"): #if it is a White bishop
                        if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "B"           
                            self.swap() #switch who's turn it is

                    else: #else it's a Black bishop
                        if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "b"           
                            self.swap() #switch who's turn it is

            elif (endCol - startCol < 0): #else if moving to left
                
                if (endRow - startRow > 0): #if moving up (according to Ben)
                    for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
                        if (self.board[startRow + i][startCol - i] != "_"): #checking if the square is empty
                            return False

                    if (piece == "B"): #if it is a White bishop
                        if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "B"           
                            self.swap() #switch who's turn it is

                    else: #else it's a Black bishop
                        if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "b"           
                            self.swap() #switch who's turn it is

                else: #else it is moving down
                    for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
                        if (self.board[startRow - i][startCol - i] != "_"): #checking if the square is empty
                            return False

                    if (piece == "B"): #if it is a White bishop
                        if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "B"           
                            self.swap() #switch who's turn it is

                    else: #else it's a Black bishop
                        if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
                            self.board[startRow][startCol] = "_"
                            self.board[endRow][endCol] = "b"           
                            self.swap() #switch who's turn it is

    def printBoard(self):
        for i in self.board:
            print(i)

    def swap(self):
        if(self.turn == "White"):
            self.turn = "Black"
        else:
            self.turn = "White"
    
var = Chess()
var.printBoard()

start = "F1"
end = "B5"

var.move(start, end)

var.printBoard()



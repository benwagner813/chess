import chess
# class Chess:

#     def __init__(self) -> None:
#         self.board = [
#             ["_","_","_","_","_","_","_","_"],#1
#             ["_","_","_","_","r","_","_","_"],#2
#             ["_","_","B","_","_","_","_","_"],#3
#             ["_","_","_","_","_","_","_","_"],#4
#             ["_","_","R","_","Q","_","_","_"],#5
#             ["_","_","_","_","_","_","_","_"],#6
#             ["_","_","B","_","_","_","_","_"],#7
#             ["_","_","_","_","_","_","_","_"] #8
#             # a   b   c   d   e   f   g   h
#         ]
#         #  [
#         #     ["R","N","B","Q","K","B","N","R"],#1
#         #     ["P","P","P","P","P","P","P","P"],#2
#         #     ["_","_","_","_","_","_","_","_"],#3
#         #     ["_","_","_","_","_","_","_","_"],#4
#         #     ["_","_","_","_","_","_","_","_"],#5
#         #     ["_","_","_","_","_","_","_","_"],#6
#         #     ["p","p","p","p","p","p","p","p"],#7
#         #     ["r","n","b","q","k","b","n","r"] #8
#         #     # a   b   c   d   e   f   g   h
#         # ]
#         self.turn = "White"

#     def is_win() -> bool:
#         pass

#     def is_draw() -> bool:
#         pass
    
#     def is_check() -> bool:
#         pass

#     def available_moves(self) -> dict:
#         listOfSquares = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8","D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8","F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8","H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]
#         available_moves = {}
#         temp_list = []
#         for string in listOfSquares: #loop through every square
#             Col = ord(string[0]) - 65
#             Row = int(string[1]) - 1

#             if(self.board[Row][Col] != "_"): #check if the square has a piece on it
#                 for string2 in listOfSquares: #for each square check if the piece can move to that square and then if true append to temp list
#                     if(self.move(string, string2)):
#                         temp_list.append(string2)
#                 if len(temp_list) > 0: #if the temp list has moves that can be made then they should be added to the available moves
#                     available_moves[string] = temp_list.copy()
#                     temp_list.clear()
#         return available_moves
                



#     def move(self, startPos:str, endPos:str) -> bool:
#         startCol = ord(startPos[0]) - 65
#         startRow = int(startPos[1]) - 1

#         endCol = ord(endPos[0]) - 65
#         endRow = int(endPos[1]) - 1

#         piece = self.board[startRow][startCol]

#         # print(self.board[endRow][endCol])

#         if (endCol in range(8) and endRow in range(8)): #if the endPos is in the bounds of the board

#             if (piece == "P" or piece == "p"): #move pawn
#                 return self.mPawn(piece, startRow, startCol, endRow, endCol)

#             elif (piece == "N" or piece == "n"): #move knight
#                 return self.mKnight(piece, startRow, startCol, endRow, endCol)
            
#             elif (piece == "K" or piece == "k"): #move king
#                 return self.mKing(piece, startRow, startCol, endRow, endCol)

#             elif (piece == "B" or piece == "b"): #move bishop
#                 return self.mBishop(piece, startRow, startCol, endRow, endCol)

#             elif (piece == "R" or piece == "r"): #move rook
#                 return self.mRook(piece, startRow, startCol, endRow, endCol)
            
#             elif (piece == "Q" or piece == "q"): #move queen
#                 return self.mQueen(piece, startRow, startCol, endRow, endCol)
        
         
#     # move pawn function
#     def mPawn(self, piece, startRow, startCol, endRow, endCol):
#         if (piece == "P"): #if the piece is a White pawn
#             if (endCol == startCol): #if endCol is same, it is trying to move

#                 if (self.board[endRow][endCol] == "_"): #the end pos is valid so it is valid

#                     if(startRow == 1): #if the pawn is on starting pos it can move two squares
#                         if(endRow == startRow + 2 and self.board[startRow + 1][startCol] == "_"): #if moving 2 square, check first square is clear
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "P"
#                             return True 
#                         elif(endRow == startRow + 1):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "P"           
#                             return True    

#                     else: #else it can only move one square
#                         if(endRow == startRow + 1):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "P"
#                             return True  
            
#             elif (endCol == startCol + 1 or endCol == startCol - 1): #if endCol is to side, it is trying to capture
                
#                 if (endRow == startRow + 1 and self.board[endRow][endCol].islower()): #if it is one row ahead and it is a Black piece
#                     # self.board[startRow][startCol] = "_"
#                     # self.board[endRow][endCol] = "P"           
#                     return True 

#         elif (piece == "p"): #if the piece is a Black pawn
#             if (endCol == startCol):

#                 if (self.board[endRow][endCol] == "_"): #the end pos is valid so it is valid

#                     if(startRow == 6): #if the pawn is on starting pos it can move two squares
#                         if(endRow == startRow - 2 and self.board[startRow - 1][startCol] == "_"): #if moving 2 square, check first square is clear
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "p"
#                             return True 
#                         elif(endRow == startRow - 1): 
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "p"
#                             return True 

#                     else: #else it can only move one square
#                         if(endRow == startRow - 1):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "p"
#                             return True 
            
#             elif (endCol == startCol + 1 or endCol == startCol - 1): #if endCol is to side, it is trying to capture
                
#                 if (endRow == startRow - 1 and self.board[endRow][endCol].isupper()): #if it is one row ahead and it is a White piece
#                     # self.board[startRow][startCol] = "_"
#                     # self.board[endRow][endCol] = "p"           
#                     return True 

#         return False #if nothing gets hit return false

#     # move knight function
#     def mKnight(self, piece, startRow, startCol, endRow, endCol):
#         if (endCol == startCol + 1 or endCol == startCol - 1): 
#             if (endRow == startRow + 2 or endRow == startRow - 2): #if end pos is up 2 over 1

#                 if (piece == "N"): #if it is a White knight
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "N"           
#                         return True 

#                 else: #else its a Black knight
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "n"           
#                         return True 

#         elif (endCol == startCol + 2 or endCol == startCol - 2):
#             if (endRow == startRow + 1 or endRow == startRow - 1): #if end pos is up 1 over 2

#                 if (piece == "N"): #if it is a White knight
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "N"           
#                         return True 

#                 else: #else its a Black knight
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "n"           
#                         return True 

#         return False #if nothing gets hit return false

#     # move king function
#     def mKing(self, piece, startRow, startCol, endRow, endCol):
#         if (startCol - 1 <= endCol <= startCol + 1 and startRow - 1 <= endRow <= startRow + 1): #if end pos is within 1 of start pos
            
#             if (piece == "K"): #if it is a White king
#                 if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                     # self.board[startRow][startCol] = "_"
#                     # self.board[endRow][endCol] = "K"           
#                     return True 

#             else: #else it's a Black king
#                 if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                     # self.board[startRow][startCol] = "_"
#                     # self.board[endRow][endCol] = "k"           
#                     return True 

#         return False #if nothing gets hit return false

#     # move bishop function
#     def mBishop(self, piece, startRow, startCol, endRow, endCol):
#         if (abs(endCol - startCol) == abs(endRow - startRow)): #if moving diagonally
            
#             if (endCol - startCol > 0): #if moving to right
                
#                 if (endRow - startRow > 0): #if moving up (according to Ben)
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow + i][startCol + i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "B"): #if it is a White bishop
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "B"           
#                             return True 

#                     else: #else it's a Black bishop
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "b"           
#                             return True 

#                 else: #else it is moving down
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow - i][startCol + i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "B"): #if it is a White bishop
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "B"           
#                             return True 

#                     else: #else it's a Black bishop
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "b"           
#                             return True 

#             elif (endCol - startCol < 0): #else if moving to left
                
#                 if (endRow - startRow > 0): #if moving up (according to Ben)
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow + i][startCol - i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "B"): #if it is a White bishop
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "B"           
#                             return True 

#                     else: #else it's a Black bishop
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "b"           
#                             return True 

#                 else: #else it is moving down
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow - i][startCol - i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "B"): #if it is a White bishop
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "B"           
#                             return True 

#                     else: #else it's a Black bishop
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "b"           
#                             return True 

#         return False #if nothing gets hit return false
    
#     def mRook(self, piece, startRow, startCol, endRow, endCol):
#         if((endRow == startRow and endCol != startCol) or (endRow != startRow and endCol == startCol)): # if moving horizontally or vertically
#             if(endCol > startCol): #moving to the right
#                 for i in range(1, abs(endCol - startCol)):
#                     if (self.board[startRow][startCol + i] != "_"): #checking if the square is empty
#                         return False
                
#                 if (piece == "R"):  #if it is a White rook
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "R"           
#                         return True 
#                 else: #else it is a Black rook
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "r"           
#                         return True 

#             if(endCol < startCol): #moving to the left
#                 for i in range(1, abs(endCol - startCol)):
#                     if (self.board[startRow][startCol - i] != "_"): #checking if the square is empty
#                         return False
               
#                 if (piece == "R"):  #if it is a White rook
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "R"           
#                         return True 
#                 else: #else it is a Black rook
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "r"           
#                         return True 

#             if(endRow > startRow): #moving up
#                 for i in range(1, abs(endRow - startRow)):
#                     if (self.board[startRow + i][startCol] != "_"): #checking if the square is empty
#                         return False
                
#                 if (piece == "R"):  #if it is a White rook
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "R"           
#                         return True 
#                 else: #else it is a Black rook
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "r"           
#                         return True 

#             if(endRow < startRow): #moving down
#                 for i in range(1, abs(endRow - startRow)):
#                     if (self.board[startRow - i][startCol] != "_"): #checking if the square is empty
#                         return False
                
#                 if (piece == "R"):  #if it is a White rook
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "R"           
#                         return True 
#                 else: #else it is a Black rook
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "r"           
#                         return True
#         return False 
    
#     def mQueen(self, piece, startRow, startCol, endRow, endCol):
#         if((endRow == startRow and endCol != startCol) or (endRow != startRow and endCol == startCol)): # if moving horizontally or vertically
#             if(endCol > startCol): #moving to the right
#                 for i in range(1, abs(endCol - startCol)):
#                     if (self.board[startRow][startCol + i] != "_"): #checking if the square is empty
#                         return False
                
#                 if (piece == "Q"):  #if it is a White queen
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "Q"           
#                         return True 
#                 else: #else it is a Black queen
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "q"           
#                         return True 

#             if(endCol < startCol): #moving to the left
#                 for i in range(1, abs(endCol - startCol)):
#                     if (self.board[startRow][startCol - i] != "_"): #checking if the square is empty
#                         return False
               
#                 if (piece == "Q"):  #if it is a White queen
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "Q"           
#                         return True 
#                 else: #else it is a Black queen
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "q"           
#                         return True 

#             if(endRow > startRow): #moving up
#                 for i in range(1, abs(endRow - startRow)):
#                     if (self.board[startRow + i][startCol] != "_"): #checking if the square is empty
#                         return False
                
#                 if (piece == "Q"):  #if it is a White queen
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "Q"           
#                         return True 
#                 else: #else it is a Black queen
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "q"           
#                         return True 

#             if(endRow < startRow): #moving down
#                 for i in range(1, abs(endRow - startRow)):
#                     if (self.board[startRow - i][startCol] != "_"): #checking if the square is empty
#                         return False
                
#                 if (piece == "Q"):  #if it is a White queen
#                     if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "Q"           
#                         return True 
#                 else: #else it is a Black queen
#                     if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                         # self.board[startRow][startCol] = "_"
#                         # self.board[endRow][endCol] = "q"           
#                         return True
#         if (abs(endCol - startCol) == abs(endRow - startRow)): #if moving diagonally
            
#             if (endCol - startCol > 0): #if moving to right
                
#                 if (endRow - startRow > 0): #if moving up (according to Ben)
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow + i][startCol + i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "B"): #if it is a White queen
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "Q"           
#                             return True 

#                     else: #else it's a Black queen
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "q"           
#                             return True 

#                 else: #else it is moving down
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow - i][startCol + i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "Q"): #if it is a White queen
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "Q"           
#                             return True 

#                     else: #else it's a Black queen
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "q"           
#                             return True 

#             elif (endCol - startCol < 0): #else if moving to left
                
#                 if (endRow - startRow > 0): #if moving up (according to Ben)
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow + i][startCol - i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "Q"): #if it is a White queen
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "Q"           
#                             return True 

#                     else: #else it's a Black queen
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "q"           
#                             return True 

#                 else: #else it is moving down
#                     for i in range(1, abs(endCol - startCol)): #checking each square inbetween start and end
#                         if (self.board[startRow - i][startCol - i] != "_"): #checking if the square is empty
#                             return False

#                     if (piece == "Q"): #if it is a White queen
#                         if (self.board[endRow][endCol].islower() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "Q"           
#                             return True 

#                     else: #else it's a Black queen
#                         if (self.board[endRow][endCol].isupper() or self.board[endRow][endCol] == "_"):
#                             # self.board[startRow][startCol] = "_"
#                             # self.board[endRow][endCol] = "q"           
#                             return True 

#         return False #if nothing gets hit return false
        




#     def printBoard(self):
#         for i in self.board:
#             print(i)

#     def swap(self) -> bool:
#         if(self.turn == "White"):
#             self.turn = "Black"
#         else:
#             self.turn = "White"
#         return True
    
# var = Chess()

# start = "F1"
# end = "B5"

# var.move(start, end)



# move_list = var.available_moves()
# for i in move_list:
#     print(i, move_list[i])

board = chess.Board()
board.push_san('e4')
board.push_san('e5')
board.push_san('Ke2')
print(board)
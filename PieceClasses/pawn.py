import pygame
from PieceClasses.piece import piece

class Pawn(piece):
    def __init__(self, color, indexIOnArray: int, indexJOnArray: int, boardArray: list[list]):
        self.promoted = False
        self.moved = False
        self.in_passante_zone = False
        super().__init__(color, indexIOnArray, indexJOnArray, boardArray)
    
    def get_image(self):
        if self.promoted:
            return pygame.image.load(f'./PieceClasses/images/{self.color}pieces/{self.color}queen.png')
        else:
            return pygame.image.load(f'./PieceClasses/images/{self.color}pieces/{self.color}pawn.png')
        
    def en_passante(self, piece):
            if self.promoted == False:
                if self.color == 'white':
                    if self.board[piece.indexI][piece.indexJ] == -1 and piece.indexI == self.indexI:
                            return [(self.indexI-1,piece.indexJ)]
                elif self.color == 'black':
                    if self.board[piece.indexI][piece.indexJ] == 1 and piece.indexI == self.indexI:
                        return [(self.indexI+1,piece.indexJ)]
                        
    def get_moves(self):
            moves = []
            if self.promoted:
                # If promoted to queen change move set
                linear = self.linear_moves()
                diagonal = self.diagonal_moves()
                return linear + diagonal
            else:
                if self.color == 'white':
                    if self.indexI-1 > 0:
                        if self.moved == False:
                            # Moves 2 ahead
                            if self.board[self.indexI-2][self.indexJ] == 0:
                                moves.append((self.indexI-2,self.indexJ))
                            # Moves 1 ahead
                            if self.board[self.indexI-1][self.indexJ] == 0:
                                moves.append((self.indexI-1,self.indexJ))
                        else:
                            # Moves 1 ahead
                            if self.board[self.indexI-1][self.indexJ] == 0:
                                moves.append((self.indexI-1,self.indexJ))
                        # Taking piece diagonally moves
                        if self.indexJ == 0:
                            if self.board[self.indexI-1][self.indexJ+1] < 0:
                                moves.append((self.indexI-1,self.indexJ+1))
                                
                        elif self.indexJ == 7:
                            if self.board[self.indexI-1][self.indexJ-1] < 0:
                                moves.append((self.indexI-1,self.indexJ-1))
                                
                        elif self.indexJ < 7 and self.indexJ > 0:
                            if self.board[self.indexI-1][self.indexJ-1] < 0:
                                moves.append((self.indexI-1,self.indexJ-1))
                                
                            if self.board[self.indexI-1][self.indexJ+1] < 0:
                                moves.append((self.indexI-1,self.indexJ+1))
                                
                        return moves
                            
                elif self.color == 'black':
                    if self.indexI + 1 < 7:
                        if self.moved == False:
                            if self.board[self.indexI+2][self.indexJ] == 0:
                                moves.append((self.indexI+2,self.indexJ))
                            if self.board[self.indexI+1][self.indexJ] == 0:
                                moves.append((self.indexI+1,self.indexJ))
                        else:
                            if self.board[self.indexI+1][self.indexJ] == 0:
                                moves.append((self.indexI+1,self.indexJ))
                        
                        # Taking piece diagonally moves
                        if self.indexJ == 0:
                            if self.board[self.indexI+1][self.indexJ+1] >= 1:
                                moves.append((self.indexI+1,self.indexJ+1))
                                
                        elif self.indexJ == 7:
                            if self.board[self.indexI+1][self.indexJ-1] >= 1:
                                moves.append((self.indexI+1,self.indexJ-1))
                                
                        elif self.indexJ < 7 and self.indexJ > 0:
                            if self.board[self.indexI+1][self.indexJ-1] >= 1:
                                moves.append((self.indexI+1,self.indexJ-1))
                                
                            if self.board[self.indexI+1][self.indexJ+1] >= 1:
                                moves.append((self.indexI+1,self.indexJ+1))
                        
                        return moves
            

    def promote_pawn(self):
            self.promoted = True
            self.surface = self.reduce_image_size()


    def diagonal_moves(self):
            moves = []
            if self.color == 'white':
                # top-right direction moves
                for x in range(1,8):
                    if self.indexI - x >= 0 and self.indexJ + x < 8: # Ensures the index does not exceed the range of the position array
                        
                        # If there is nothing blocking the bishops way then add it to potential moves or
                        # If it detects a piece of the opposite colour, add it to the potential moves 
                        if self.board[self.indexI-x][self.indexJ + x] < 1:
                            moves.append((self.indexI-x, self.indexJ + x))
                            
                        # break if the position has a piece of the same colour stop as only knights can jump same coloured pieces
                        else:
                            break
                        
                        # So it does not add moves that are past the point of the opposite piece
                        if self.board[self.indexI-x][self.indexJ + x] < 0:
                            break
                        
                # bottom-right direction moves
                for x in range(1,8):
                    if self.indexI + x < 8 and self.indexJ + x < 8:
                        if self.board[self.indexI+x][self.indexJ + x] < 1:
                            moves.append((self.indexI+x, self.indexJ + x))
                        else:
                            break
                        if self.board[self.indexI+x][self.indexJ + x] < 0:
                            break
                # bottom-left direction moves
                for x in range(1,8):
                    if self.indexI + x < 8 and self.indexJ - x >= 0:
                        if self.board[self.indexI+x][self.indexJ-x] < 1:
                            moves.append((self.indexI+x, self.indexJ-x))
                        else:
                            break
                        if self.board[self.indexI+x][self.indexJ-x] < 0:
                            break
                # Left direction moves
                for x in range(1,8):
                    if self.indexI - x >= 0 and self.indexJ - x >=0:
                        if self.board[self.indexI-x][self.indexJ-x] < 1:
                            moves.append((self.indexI-x, self.indexJ-x))
                        else:
                            break
                        if self.board[self.indexI-x][self.indexJ-x] < 0:
                            break
                return moves
            
            elif self.color == 'black':
                # top-right direction moves
                for x in range(1,8):
                    if self.indexI - x >= 0 and self.indexJ + x < 8: # Ensures the index does not exceed the range of the position array
                        
                        # If there is nothing blocking the bishops way then add it to potential moves or
                        # If it detects a piece of the opposite colour, add it to the potential moves 
                        if self.board[self.indexI-x][self.indexJ + x] > -1:
                            moves.append((self.indexI-x, self.indexJ + x))
                            
                        # break if the position has a piece of the same colour stop as only knights can jump same coloured pieces
                        else:
                            break
                        
                        # So it does not add moves that are past the point of the opposite piece
                        if self.board[self.indexI-x][self.indexJ + x] > 0:
                            break
                        
                # bottom-right direction moves
                for x in range(1,8):
                    if self.indexI + x < 8 and self.indexJ + x < 8:
                        if self.board[self.indexI+x][self.indexJ + x] > -1:
                            moves.append((self.indexI+x, self.indexJ + x))
                        else:
                            break
                        if self.board[self.indexI+x][self.indexJ + x] > 0:
                            break
                # bottom-left direction moves
                for x in range(1,8):
                    if self.indexI + x < 8 and self.indexJ - x >= 0:
                        if self.board[self.indexI+x][self.indexJ-x] > -1:
                            moves.append((self.indexI+x, self.indexJ-x))
                        else:
                            break
                        if self.board[self.indexI+x][self.indexJ-x] > 0:
                            break
                # Left direction moves
                for x in range(1,8):
                    if self.indexI - x >= 0 and self.indexJ - x >=0:
                        if self.board[self.indexI-x][self.indexJ-x] > -1:
                            moves.append((self.indexI-x, self.indexJ-x))
                        else:
                            break
                        if self.board[self.indexI-x][self.indexJ-x] > 0:
                            break
                return moves
    
    def linear_moves(self):
            moves = []
            if self.color == 'white':
                # Up direction moves
                for x in range(1,8):
                    if self.indexI - x >= 0: # Ensures the index does not exceed the range of the position array
                        
                        # If there is nothing blocking the castles way then add it to potential moves or
                        # If it detects a piece of the opposite colour, add it to the potential moves 
                        if self.board[self.indexI-x][self.indexJ] < 1:
                            moves.append((self.indexI-x, self.indexJ))
                            
                        # break if the position has a piece of the same colour stop as only knights can jump same coloured pieces
                        else:
                            break
                        
                        # So it does not add moves that are past the point of the opposite piece
                        if self.board[self.indexI-x][self.indexJ] < 0:
                            break
                        
                # Down direction moves
                for x in range(1,8):
                    if self.indexI + x < 8:
                        if self.board[self.indexI+x][self.indexJ] < 1:
                            moves.append((self.indexI+x, self.indexJ))
                        else:
                            break
                        if self.board[self.indexI+x][self.indexJ] < 0:
                            break
                # Right direction moves
                for x in range(1,8):
                    if self.indexJ + x < 8:
                        if self.board[self.indexI][self.indexJ+x] < 1:
                            moves.append((self.indexI, self.indexJ+x))
                        else:
                            break
                        if self.board[self.indexI][self.indexJ+x] < 0:
                            break
                # Left direction moves
                for x in range(1,8):
                    if self.indexJ - x >= 0:
                        if self.board[self.indexI][self.indexJ-x] < 1:
                            moves.append((self.indexI, self.indexJ-x))
                        else:
                            break
                        if self.board[self.indexI][self.indexJ-x] < 0:
                            break
                return moves
                        
            elif self.color == 'black':
                # Up direction moves
                for x in range(1,8):
                    if self.indexI - x >= 0: # Ensures the index does not exceed the range of the position array
                        
                        # If there is nothing blocking the castles way then add it to potential moves or
                        # If it detects a piece of the opposite colour, add it to the potential moves 
                        if self.board[self.indexI-x][self.indexJ] > -1:
                            moves.append((self.indexI-x, self.indexJ))
                            
                        # break if the position has a piece of the same colour stop as only knights can jump same coloured pieces
                        else:
                            break
                        
                        # So it does not add moves that are past the point of the opposite piece
                        if self.board[self.indexI-x][self.indexJ] > 0:
                            break
                        
                # Down direction moves
                for x in range(1,8):
                    if self.indexI + x < 8:
                        if self.board[self.indexI+x][self.indexJ] > -1:
                            moves.append((self.indexI+x, self.indexJ))
                        else:
                            break
                        if self.board[self.indexI+x][self.indexJ] > 0:
                            break
                # Right direction moves
                for x in range(1,8):
                    if self.indexJ + x < 8:
                        if self.board[self.indexI][self.indexJ+x] > -1:
                            moves.append((self.indexI, self.indexJ+x))
                        else:
                            break
                        if self.board[self.indexI][self.indexJ+x] > 0:
                            break
                # Left direction moves
                for x in range(1,8):
                    if self.indexJ - x >= 0:
                        if self.board[self.indexI][self.indexJ-x] > -1:
                            moves.append((self.indexI, self.indexJ-x))
                        else:
                            break
                        if self.board[self.indexI][self.indexJ-x] > 0:
                            break
                return moves
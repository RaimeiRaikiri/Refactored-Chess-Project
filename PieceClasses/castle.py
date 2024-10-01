import pygame
from PieceClasses.piece import piece

class Castle(piece):
    
    def __init__(self, color, indexIOnArray: int, indexJOnArray: int, boardArray: list[list]):
        super().__init__(color, indexIOnArray, indexJOnArray, boardArray)
        self.moved = False
        
    def get_image(self):
            return pygame.image.load(f'./PieceClasses/images/{self.color}pieces/{self.color}castle.png')
    
    def get_moves(self)->list[tuple]:
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
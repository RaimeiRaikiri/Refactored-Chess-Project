import pygame
from PieceClasses.piece import piece

class Knight(piece):
    
    def __init__(self, color, indexIOnArray: int, indexJOnArray: int, boardArray: list[list]):
        super().__init__(color, indexIOnArray, indexJOnArray, boardArray)
    
    def get_image(self):
        return pygame.image.load(f'./PieceClasses/images/{self.color}pieces/{self.color}knight.png')
    
    def get_moves(self):
        if self.onBoard:
            moves = []
            if self.color == 'white':
                # Down - Changing index I by 2 
                
                    # Right - Changing index J by 1
                if self.indexI + 2 < 8 and self.indexJ + 1 < 8:
                    if self.board[self.indexI + 2][self.indexJ + 1] < 1:
                        moves.append(self.board[self.indexI + 2][self.indexJ + 1])
                    # Left - Changing index J by 1
                if self.indexI + 2 < 8 and self.indexJ - 1 >=0:
                    if self.board[self.indexI + 2][self.indexJ - 1] < 1:
                        moves.append(self.board[self.indexI + 2][self.indexJ - 1])
                # Up - Changing index I by 2
                   
                   # Right - Changing index J by 1
                if self.indexI - 2 >= 0 and self.indexJ + 1 < 8:
                    if self.board[self.indexI - 2][self.indexJ + 1] < 1:
                        moves.append(self.board[self.indexI - 2][self.indexJ + 1])
                    # Left - Changing index J by 1
                if self.indexI - 2 >= 0 and self.indexJ - 1 >=0:
                    if self.board[self.indexI - 2][self.indexJ - 1] < 1:
                        moves.append(self.board[self.indexI - 2][self.indexJ - 1])
                # Right - Changing J index by 2
                
                    # Down - Changing I index by 1
                if self.indexI + 1 < 8 and self.indexJ + 2 < 8:
                    if self.board[self.indexI + 1][self.indexJ + 2] < 1:
                        moves.append(self.board[self.indexI + 1][self.indexJ + 2])
                    # Up - Changing I index by 1
                if self.indexI - 1 >= 0 and self.indexJ + 2 < 8:
                    if self.board[self.indexI - 1][self.indexJ + 2] < 1:
                        moves.append(self.board[self.indexI - 1][self.indexJ + 2])
                # Left - Changing J index by 2
                
                    # Down - Changing I index by 1
                if self.indexI + 1 < 8 and self.indexJ - 2 >=0:
                    if self.board[self.indexI + 1][self.indexJ - 2] < 1:
                        moves.append(self.board[self.indexI + 1][self.indexJ - 2])
                    # Up - Changing I index by 1
                if self.indexI - 1 >= 0 and self.indexJ - 2 >=0:
                    if self.board[self.indexI - 1][self.indexJ - 2] < 1:
                        moves.append(self.board[self.indexI - 1][self.indexJ - 2])
                
                return moves
                        
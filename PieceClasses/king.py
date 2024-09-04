import pygame
from PieceClasses.piece import piece

class King(piece):
    def __init__(self, color, indexIOnArray: int, indexJOnArray: int, boardArray: list[list]):
        super().__init__(color, indexIOnArray, indexJOnArray, boardArray)
    
    def get_image(self):
        return pygame.image.load(f'./PieceClasses/images/{self.color}pieces/{self.color}king.png')

    def get_moves(self):
            moves = []
            if self.color == 'white':
                # top
                if self.indexI - 1 < 8:
                    if self.board[self.indexI-1][self.indexJ] < 1:
                        moves.append((self.indexI-1,self.indexJ))
                # top-right
                if self.indexI - 1 < 8 and self.indexJ + 1 < 8:
                    if self.board[self.indexI-1][self.indexJ+1] < 1:
                        moves.append((self.indexI-1,self.indexJ+1))
                # right
                if self.indexJ + 1 < 8:
                    if self.board[self.indexI][self.indexJ+1] < 1:
                        moves.append((self.indexI,self.indexJ+1))
                # bottom-right
                if self.indexI + 1 < 8 and self.indexJ + 1 < 8:
                    if self.board[self.indexI + 1][self.indexJ + 1] < 1:
                        moves.append((self.indexI+1,self.indexJ+1))
                # bottom
                if self.indexI + 1 < 8:
                    if self.board[self.indexI+1][self.indexJ] < 1:
                        moves.append((self.indexI+1,self.indexJ))
                # bottom-left
                if self.indexI + 1 < 8 and self.indexJ - 1 >=0:
                    if self.board[self.indexI +1][self.indexJ -1] < 1:
                        moves.append((self.indexI+1, self.indexJ-1))
                # left
                if self.indexJ - 1 >=0:
                    if self.board[self.indexI][self.indexJ-1] < 1:
                        moves.append((self.indexI,self.indexJ-1))
                # top-left
                if self.indexI - 1 < 8 and self.indexJ-1 >=0:
                    if self.board[self.indexI-1][self.indexJ-1] < 1:
                        moves.append((self.indexI-1,self.indexJ-1))
                
                return moves
            elif self.color == 'black':
                # top
                if self.indexI - 1 < 8:
                    if self.board[self.indexI-1][self.indexJ] >= 0:
                        moves.append((self.indexI-1,self.indexJ))
                # top-right
                if self.indexI - 1 < 8 and self.indexJ + 1 < 8:
                    if self.board[self.indexI-1][self.indexJ+1] >= 0:
                        moves.append((self.indexI-1,self.indexJ+1))
                # right
                if self.indexJ + 1 < 8:
                    if self.board[self.indexI][self.indexJ+1] >= 0:
                        moves.append((self.indexI,self.indexJ+1))
                # bottom-right
                if self.indexI + 1 < 8 and self.indexJ + 1 < 8:
                    if self.board[self.indexI + 1][self.indexJ + 1] >= 0:
                        moves.append((self.indexI+1,self.indexJ+1))
                # bottom
                if self.indexI + 1 < 8:
                    if self.board[self.indexI+1][self.indexJ] >= 0:
                        moves.append((self.indexI+1,self.indexJ))
                # bottom-left
                if self.indexI + 1 < 8 and self.indexJ - 1 >=0:
                    if self.board[self.indexI +1][self.indexJ -1] >= 0:
                        moves.append((self.indexI+1, self.indexJ-1))
                # left
                if self.indexJ - 1 >=0:
                    if self.board[self.indexI][self.indexJ-1] >= 0:
                        moves.append((self.indexI,self.indexJ-1))
                # top-left
                if self.indexI - 1 < 8 and self.indexJ-1 >=0:
                    if self.board[self.indexI-1][self.indexJ-1] >= 0:
                        moves.append((self.indexI-1,self.indexJ-1))
                
                return moves
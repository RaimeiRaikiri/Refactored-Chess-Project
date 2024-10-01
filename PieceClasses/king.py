import pygame
from PieceClasses.piece import piece

class King(piece):
    def __init__(self, color, indexIOnArray: int, indexJOnArray: int, boardArray: list[list]):
        super().__init__(color, indexIOnArray, indexJOnArray, boardArray)
        self.moved = False
    
    def get_image(self):
        return pygame.image.load(f'./PieceClasses/images/{self.color}pieces/{self.color}king.png')

    def get_moves(self, castle1, castle2, opposition_moves):
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
                
                # Castling
                if self.moved == False and castle1.moved == False:
                    # Long side
                    
                    # Spaces between king and castle empty
                    if self.board[self.indexI][self.indexJ - 1] == 0 and self.board[self.indexI][self.indexJ - 2] == 0 and self.board[self.indexI][self.indexJ - 3] == 0:
                        moves.append((self.indexI, self.indexJ-2))
                        spaces = [(self.indexI, self.indexJ),(self.indexI, self.indexJ -1), (self.indexI,self.indexJ-2), (self.indexI, self.indexJ-3)]
                        for space in spaces:
                            if space in opposition_moves:
                                moves.pop()
                                break
                    
                if self.moved == False and castle2.moved == False:
                    # Short side
                    
                    # Spaces between king and castle empty
                    if self.board[self.indexI][self.indexJ + 1] == 0 and self.board[self.indexI][self.indexJ + 2] == 0:
                        moves.append((self.indexI, self.indexJ+2))
                        spaces = [(self.indexI, self.indexJ),(self.indexI, self.indexJ +1), (self.indexI,self.indexJ+2)]
                        for space in spaces:
                            if space in opposition_moves:
                                moves.pop()
                                break
                
                return moves
            
            elif self.color == 'black':
                # top
                if self.indexI - 1 >= 0:
                    if self.board[self.indexI-1][self.indexJ] >= 0:
                        moves.append((self.indexI-1,self.indexJ))
                # top-right
                if self.indexI - 1 >= 0 and self.indexJ + 1 < 8:
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
                if self.indexI - 1 >= 0 and self.indexJ-1 >= 0:
                    if self.board[self.indexI-1][self.indexJ-1] >= 0:
                        moves.append((self.indexI-1,self.indexJ-1))
                
                # Castling
                if self.moved == False and castle1.moved == False:
                    # Long side
                    
                    # Spaces between king and castle empty
                    if self.board[self.indexI][self.indexJ - 1] == 0 and self.board[self.indexI][self.indexJ - 2] == 0 and self.board[self.indexI][self.indexJ - 3] == 0:
                        moves.append((self.indexI, self.indexJ-2))
                        spaces = [(self.indexI, self.indexJ),(self.indexI, self.indexJ -1), (self.indexI,self.indexJ-2), (self.indexI, self.indexJ-3)]
                        for space in spaces:
                            if space in opposition_moves:
                                moves.pop()
                                break
                    
                if self.moved == False and castle2.moved == False:
                    # Short side
                    
                    # Spaces between king and castle empty
                    if self.board[self.indexI][self.indexJ + 1] == 0 and self.board[self.indexI][self.indexJ + 2] == 0:
                        moves.append((self.indexI, self.indexJ+2))
                        spaces = [(self.indexI, self.indexJ),(self.indexI, self.indexJ +1), (self.indexI,self.indexJ+2)]
                        for space in spaces:
                            if space in opposition_moves:
                                moves.pop()
                                break
                
                return moves
import pygame

class piece:
    
    def __init__(self, color, indexIOnArray: int, indexJOnArray: int, boardArray = list[list]):
        # Visual variables
        self.size = (50,50)
        self.color = color
        self.surface = self.reduce_image_size()
        self.rect =  self.surface.get_rect(center=(300,100))
        
        # Positional variables
        self.indexI = indexIOnArray
        self.indexJ = indexJOnArray
        self.moves = None
        self.board = boardArray
        self.onBoard = True
    
    
    # Get image and fit it to size of piece
    def get_image(self):
        # function to be overriden
        pass
    def reduce_image_size(self):
        return pygame.transform.scale(self.get_image(), self.size)
        
import pygame

class piece:
    
    def __init__(self, color, indexIOnArray: int, indexJOnArray: int, boardArray: list[list]):
        # Positional variables
        self.indexI = indexIOnArray
        self.indexJ = indexJOnArray
        self.board = boardArray
        self.x, self.y = self.get_position()
        
        # Visual variables
        self.size = (50,50)
        self.color = color
        self.surface = self.reduce_image_size()
        self.rect =  self.surface.get_rect(center=(self.x, self.y))
        
    
    
    # Get image and fit it to size of piece
    def get_image(self):
        # function to be overriden
        pass
    def reduce_image_size(self):
        return pygame.transform.scale(self.get_image(), self.size)
        
    # Initial position set by index position
    def get_position(self):
        return (((self.indexJ+1)*100)+200 , ((self.indexI+1)*100) +80)
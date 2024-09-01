import pygame

class piece:
    
    def __init__(self, color, indexIOnArray = int, indexJOnArray = int):
        # Visual variables
        self.size = (50,50)
        self.color = color
        self.surface = self.reduce_image_size()
        self.rect =  self.surface.get_rect(center=(300,100))
        
        # Positional variables
        self.indexI = indexIOnArray
        self.indexJ = indexJOnArray
        self.position = self.get_position()
        self.moves = None
    
    
    # Get image and fit it to size of piece
    def get_image(self):
        # function to be overriden
        pass
    def reduce_image_size(self):
        return pygame.transform.scale(self.get_image(), self.size)
        
    def get_position(self):
        if self.indexI == 0:
            if self.indexJ == 0:
                return ('a', 8)
            if self.indexJ == 1:
                return ('b', 8)
            if self.indexJ == 2:
                return ('c', 8)
            if self.indexJ == 3:
                return ('d', 8)
            if self.indexJ == 4:
                return ('e', 8)
            if self.indexJ == 5:
                return ('f', 8)
            if self.indexJ == 6:
                return ('g', 8)
            if self.indexJ == 7:
                return ('h', 8)
            
        if self.indexI == 1:
            if self.indexJ == 0:
                return ('a', 7)
            if self.indexJ == 1:
                return ('b', 7)
            if self.indexJ == 2:
                return ('c', 7)
            if self.indexJ == 3:
                return ('d', 7)
            if self.indexJ == 4:
                return ('e', )
            if self.indexJ == 5:
                return ('f', 7)
            if self.indexJ == 6:
                return ('g', 7)
            if self.indexJ == 7:
                return ('h', 7)
            
        if self.indexI == 2:
            if self.indexJ == 0:
                return ('a', 6)
            if self.indexJ == 1:
                return ('b', 6)
            if self.indexJ == 2:
                return ('c', 6)
            if self.indexJ == 3:
                return ('d', 6)
            if self.indexJ == 4:
                return ('e', 6)
            if self.indexJ == 5:
                return ('f', 6)
            if self.indexJ == 6:
                return ('g', 6)
            if self.indexJ == 7:
                return ('h', 6)
        
        if self.indexI == 3:
            if self.indexJ == 0:
                return ('a', 5)
            if self.indexJ == 1:
                return ('b', 5)
            if self.indexJ == 2:
                return ('c', 5)
            if self.indexJ == 3:
                return ('d', 5)
            if self.indexJ == 4:
                return ('e', 5)
            if self.indexJ == 5:
                return ('f', 5)
            if self.indexJ == 6:
                return ('g', 5)
            if self.indexJ == 7:
                return ('h', 5)
            
        if self.indexI == 4:
            if self.indexJ == 0:
                return ('a', 4)
            if self.indexJ == 1:
                return ('b', 4)
            if self.indexJ == 2:
                return ('c', 4)
            if self.indexJ == 3:
                return ('d', 4)
            if self.indexJ == 4:
                return ('e', 4)
            if self.indexJ == 5:
                return ('f', 4)
            if self.indexJ == 6:
                return ('g', 4)
            if self.indexJ == 7:
                return ('h', 4)
        
        if self.indexI == 5:
            if self.indexJ == 0:
                return ('a', 3)
            if self.indexJ == 1:
                return ('b', 3)
            if self.indexJ == 2:
                return ('c', 3)
            if self.indexJ == 3:
                return ('d', 3)
            if self.indexJ == 4:
                return ('e', 3)
            if self.indexJ == 5:
                return ('f', 3)
            if self.indexJ == 6:
                return ('g', 3)
            if self.indexJ == 7:
                return ('h', 3)
        
        if self.indexI == 6:
            if self.indexJ == 0:
                return ('a', 2)
            if self.indexJ == 1:
                return ('b', 2)
            if self.indexJ == 2:
                return ('c', 2)
            if self.indexJ == 3:
                return ('d', 2)
            if self.indexJ == 4:
                return ('e', 2)
            if self.indexJ == 5:
                return ('f', 2)
            if self.indexJ == 6:
                return ('g', 2)
            if self.indexJ == 7:
                return ('h', 2)
        
        if self.indexI == 7:
            if self.indexJ == 0:
                return ('a', 1)
            if self.indexJ == 1:
                return ('b', 1)
            if self.indexJ == 2:
                return ('c', 1)
            if self.indexJ == 3:
                return ('d', 1)
            if self.indexJ == 4:
                return ('e', 1)
            if self.indexJ == 5:
                return ('f', 1)
            if self.indexJ == 6:
                return ('g', 1)
            if self.indexJ == 7:
                return ('h', 1)
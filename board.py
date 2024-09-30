import pygame
class Board:
    def __init__(self):
        # Positions of pieces on game start
        # 0 = Empty space
        # 1 = pawn -1 if black
        # 2 = castle -2 if black
        # 3 = knight -3 if black    
        # 4 = bishop -4 if black
        # 5 = queen -5 if black
        # 6 = king -6 if black
        self.positionArray = [[-2,-3,-4,-5,-6,-4,-3,-2],
                              [-1 for x in range(0,8)],
                              [0 for x in range(0,8)],
                              [0 for x in range(0,8)],
                              [0 for x in range(0,8)],
                              [0 for x in range(0,8)],
                              [1 for x in range(0,8)],
                              [2,3,4,5,6,4,3,2]]
        # Create all tiles and put them in the correct position in relation to the position array and in relation to the screen
        
        # The tiles are positioned in an array in alignment with
        # the position array so they can be accessed using the same indexes as the pieces position
        self.tileArray = [[pygame.Rect((100*x)+200,80,100,100) for x in range(8)],
                          [pygame.Rect((100*x)+200,180,100,100) for x in range(8)],
                          [pygame.Rect((100*x)+200,280,100,100) for x in range(8)],
                          [pygame.Rect((100*x)+200,380,100,100) for x in range(8)],
                          [pygame.Rect((100*x)+200,480,100,100) for x in range(8)],
                          [pygame.Rect((100*x)+200,580,100,100) for x in range(8)],
                          [pygame.Rect((100*x)+200,680,100,100) for x in range(8)],
                          [pygame.Rect((100*x)+200,780,100,100) for x in range(8)]]
        
        self.drawArray = [[pygame.Rect(100*x,0,100,100) for x in range(8)],
                          [pygame.Rect(100*x,100,100,100) for x in range(8)],
                          [pygame.Rect(100*x,200,100,100) for x in range(8)],
                          [pygame.Rect(100*x,300,100,100) for x in range(8)],
                          [pygame.Rect(100*x,400,100,100) for x in range(8)],
                          [pygame.Rect(100*x,500,100,100) for x in range(8)],
                          [pygame.Rect(100*x,600,100,100) for x in range(8)],
                          [pygame.Rect(100*x,700,100,100) for x in range(8)]]
        # Surface to put all the tiles on and the place on the screen on game start
        self.surface = pygame.Surface((800,800))
        
        # Added alternating black and white tiles to the surface
        for x in range(8):
            if x == 0 or x % 2 == 0:  
                for y in range(8):
                    if y == 0 or y % 2 == 0:
                        pygame.draw.rect(self.surface, 'white', self.drawArray[x][y])
                    else:
                        pygame.draw.rect(self.surface, 'black', self.drawArray[x][y])
            else:
                for y in range(8):
                    if y == 0 or y % 2 == 0:
                        pygame.draw.rect(self.surface, 'black', self.drawArray[x][y])
                    else:
                        pygame.draw.rect(self.surface, 'white', self.drawArray[x][y])
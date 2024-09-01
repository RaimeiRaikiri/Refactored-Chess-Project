import pygame, sys, PieceClasses
from board import Board

pygame.init()
clock =  pygame.time.Clock()
screenWidth, screenHeight = 1200, 1200
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('2-Player Chess')
boards = Board()

def DrawBoardBorder():
    # Draws a rect border around the board to prevent the pieces from leaving the board
    pygame.draw.rect(screen, (0,0,0), boards.surface.get_rect(topleft=(200,100)), width = 2)
    
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    screen.fill('white')
    screen.blit(boards.surface, (200,100))
    DrawBoardBorder()
                
    pygame.display.flip()
    clock.tick(60)
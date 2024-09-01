import pygame, sys, PieceClasses
from board import Board

pygame.init()
clock =  pygame.time.Clock()
screenWidth, screenHeight = 1200, 1200
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('2-Player Chess')
boards = Board()

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    screen.fill('black')
    screen.blit(boards.surface, (0,0))
                
    pygame.display.flip()
    clock.tick(60)
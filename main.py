import pygame, sys, PieceClasses
from board import Board

pygame.init()
clock =  pygame.time.Clock()
screenWidth, screenHeight = 1200, 1200
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('2-Player Chess')

board = Board()
collisionlist = sum(board.tileArray, [])

# white pieces
whitecastle1 =  PieceClasses.Castle('white', 7,0,board.positionArray)
whitecastle2 =  PieceClasses.Castle('white', 7,7,board.positionArray)

# black pieces
blackcastle1 =  PieceClasses.Castle('black', 0,0,board.positionArray)
blackcastle2 =  PieceClasses.Castle('black', 0,7,board.positionArray)

def DrawBoardBorder():
    # Draws a rect border around the board to prevent the pieces from leaving the board
    pygame.draw.rect(screen, (0,0,0), board.surface.get_rect(), width = 2)
# Updates the position array for every piece after every turn so the correct moves can be decided
def UpdateBoard(piece):
    piece.board = board.positionArray

def center_pieces(*pieces):
    for piece in pieces:
        if piece.rect.collidelist(collisionlist) != -1:
            piece.rect.center = collisionlist[piece.rect.collidelist(collisionlist)].center 

    
def put_pieces_on_board():
    screen.blit(whitecastle1.surface, whitecastle1.rect)
    screen.blit(whitecastle2.surface, whitecastle2.rect)
    screen.blit(blackcastle1.surface, blackcastle1.rect)
    screen.blit(blackcastle2.surface, blackcastle2.rect)
    
    
    
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    screen.fill('white')
    # Board set up
    screen.blit(board.surface, (0,0))
    DrawBoardBorder()
    put_pieces_on_board()
    center_pieces(whitecastle1, whitecastle2, blackcastle1, blackcastle2)
    
    UpdateBoard(whitecastle1)
    pygame.display.flip()
    clock.tick(60)
import pygame, sys, PieceClasses
from board import Board

pygame.init()
clock =  pygame.time.Clock()
screenWidth, screenHeight = 1200, 1200
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('2-Player Chess')

board = Board()
# 2d array flattened to 1d so collidelist method can work
collisionlist = sum(board.tileArray, [])


# white pieces
whitecastle1 =  PieceClasses.Castle('white', 7,0,board.positionArray)
whitecastle2 =  PieceClasses.Castle('white', 7,7,board.positionArray)
# list of all white pieces
white_pieces = [whitecastle1, whitecastle2]


# black pieces
blackcastle1 =  PieceClasses.Castle('black', 0,0,board.positionArray)
blackcastle2 =  PieceClasses.Castle('black', 0,7,board.positionArray)
# list of all black pieces 
black_pieces = [blackcastle1.rect, blackcastle2.rect]
def DrawBoardBorder():
    # Draws a rect border around the board to prevent the pieces from leaving the board
    pygame.draw.rect(screen, (0,0,0), board.surface.get_rect(), width = 2)
# Updates the position array for every piece after every turn so the correct moves can be decided
def UpdateBoard(piece):
    piece.board = board.positionArray

# Can take any number of chess pieces and center them in the tile they're on
def center_pieces(*pieces):
    for piece in pieces:
        if piece.rect.collidelist(collisionlist) != -1:
            piece.rect.center = collisionlist[piece.rect.collidelist(collisionlist)].center 

    
def put_pieces_on_board():
    screen.blit(whitecastle1.surface, whitecastle1.rect)
    screen.blit(whitecastle2.surface, whitecastle2.rect)
    screen.blit(blackcastle1.surface, blackcastle1.rect)
    screen.blit(blackcastle2.surface, blackcastle2.rect)
    
    center_pieces(whitecastle1, whitecastle2, blackcastle1, blackcastle2)

def which_piece_mouse_selects():
    if white_players_turn and mouse_point.collidelist(white_pieces) != -1:
        return white_pieces[mouse_point.collidelist(white_pieces)]
    elif not white_players_turn and mouse_point.collidelist(black_pieces) != -1:
        return black_pieces[mouse_point.collidelist(black_pieces)]

mouse_point = pygame.Rect(1100,1100,1,1)
def mouse_tracking(whereMouseIs):
    mouse_point.x, mouse_point.y = whereMouseIs
    pygame.draw.rect(screen, (0,0,0), mouse_point, width = 0)
def check_mouse_in_border(whereMouseIs):
    if board.surface.get_rect().collidepoint(whereMouseIs):
        return True
    else:
        return False
    
    
game_over = False
# If not white players turn it is black players
white_players_turn = True
current_moving_piece = None
while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over:
                pass
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_tracking(whereMouseIs)
                    current_moving_piece = which_piece_mouse_selects()
                if event.type == pygame.MOUSEBUTTONUP and check_mouse_in_border(whereMouseIs):
                    if current_moving_piece:
                        current_moving_piece.rect.topleft = whereMouseIs
                        center_pieces(current_moving_piece)
                    
    screen.fill('white')
    whereMouseIs = pygame.mouse.get_pos()
    # Board set up
    screen.blit(board.surface, (0,0))
    DrawBoardBorder()
    put_pieces_on_board()
    
    UpdateBoard(whitecastle1)
    pygame.display.flip()
    clock.tick(60)
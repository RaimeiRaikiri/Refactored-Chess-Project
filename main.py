import pygame, sys, PieceClasses
import PieceClasses.queen
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
whitebishop1 =  PieceClasses.Bishop('white', 7,2,board.positionArray)
whitebishop2 =  PieceClasses.Bishop('white', 7,5,board.positionArray)
whitequeen = PieceClasses.Queen('white',7,4, board.positionArray )
whiteknight1 = PieceClasses.Knight('white', 7,1, board.positionArray)
whiteknight2 = PieceClasses.Knight('white', 7,6, board.positionArray)
whitepawn1 = PieceClasses.Pawn('white', 6,0,board.positionArray)
whitepawn2 = PieceClasses.Pawn('white', 6,1,board.positionArray)
whitepawn3 = PieceClasses.Pawn('white', 6,2,board.positionArray)
whitepawn4 = PieceClasses.Pawn('white', 6,3,board.positionArray)
whitepawn5 = PieceClasses.Pawn('white', 6,4,board.positionArray)
whitepawn6 = PieceClasses.Pawn('white', 6,5,board.positionArray)
whitepawn7 = PieceClasses.Pawn('white', 6,6,board.positionArray)
whitepawn8 = PieceClasses.Pawn('white', 6,7,board.positionArray)


# list of all white pieces
white_pieces = [whitecastle1, whitecastle2, whitebishop1, whitebishop2, whitequeen, whiteknight1, whiteknight2, whitepawn1,whitepawn2,whitepawn3,whitepawn4,whitepawn5,whitepawn6,whitepawn7,whitepawn8]
white_pawns = [whitepawn1,whitepawn2,whitepawn3,whitepawn4,whitepawn5,whitepawn6,whitepawn7,whitepawn8]
whitePawnPromotionZone = [tile for tile in board.tileArray[0]]
whiteEnPassanteZone = [tile for tile in board.tileArray[3]]

# black pieces
blackcastle1 =  PieceClasses.Castle('black', 0,0,board.positionArray)
blackcastle2 =  PieceClasses.Castle('black', 0,7,board.positionArray)
blackbishop1 =  PieceClasses.Bishop('black', 0,2,board.positionArray)
blackbishop2 =  PieceClasses.Bishop('black', 0,5,board.positionArray)
blackqueen = PieceClasses.Queen('black', 0,4,board.positionArray)
blackknight1 = PieceClasses.Knight('black', 0,1,board.positionArray)
blackknight2 = PieceClasses.Knight('black', 0,6,board.positionArray)
blackpawn1 = PieceClasses.Pawn('black', 1,0,board.positionArray)
blackpawn2 = PieceClasses.Pawn('black', 1,1,board.positionArray)
blackpawn3 = PieceClasses.Pawn('black', 1,2,board.positionArray)
blackpawn4 = PieceClasses.Pawn('black', 1,3,board.positionArray)
blackpawn5 = PieceClasses.Pawn('black', 1,4,board.positionArray)
blackpawn6 = PieceClasses.Pawn('black', 1,5,board.positionArray)
blackpawn7 = PieceClasses.Pawn('black', 1,6,board.positionArray)
blackpawn8 = PieceClasses.Pawn('black', 1,7,board.positionArray)


# list of all black pieces 
black_pieces = [blackcastle1, blackcastle2, blackbishop1, blackbishop2, blackqueen, blackknight1, blackknight2, blackpawn1, blackpawn2, blackpawn3, blackpawn4, blackpawn5,blackpawn6,blackpawn7,blackpawn8]
black_pawns = [blackpawn1, blackpawn2, blackpawn3, blackpawn4, blackpawn5,blackpawn6,blackpawn7,blackpawn8]
blackPawnPromotionZone = [tile for tile in board.tileArray[7]]
blackEnPassanteZone = [tile for tile in board.tileArray[4]]

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
    screen.blit(whitebishop1.surface, whitebishop1.rect)
    screen.blit(whitebishop2.surface, whitebishop2.rect)
    screen.blit(whitequeen.surface, whitequeen.rect)
    screen.blit(whiteknight1.surface, whiteknight1.rect)
    screen.blit(whiteknight2.surface, whiteknight2.rect)
    screen.blit(whitepawn1.surface,whitepawn1.rect)
    screen.blit(whitepawn2.surface,whitepawn2.rect)
    screen.blit(whitepawn3.surface,whitepawn3.rect)
    screen.blit(whitepawn4.surface,whitepawn4.rect)
    screen.blit(whitepawn5.surface,whitepawn5.rect)
    screen.blit(whitepawn6.surface,whitepawn6.rect)
    screen.blit(whitepawn7.surface,whitepawn7.rect)
    screen.blit(whitepawn8.surface,whitepawn8.rect)
    
    
    screen.blit(blackcastle1.surface, blackcastle1.rect)
    screen.blit(blackcastle2.surface, blackcastle2.rect)
    screen.blit(blackbishop1.surface, blackbishop1.rect)
    screen.blit(blackbishop2.surface, blackbishop2.rect)
    screen.blit(blackqueen.surface, blackqueen.rect)
    screen.blit(blackknight1.surface, blackknight1.rect)
    screen.blit(blackknight2.surface, blackknight2.rect)
    screen.blit(blackpawn1.surface,blackpawn1.rect)
    screen.blit(blackpawn2.surface,blackpawn2.rect)
    screen.blit(blackpawn3.surface,blackpawn3.rect)
    screen.blit(blackpawn4.surface,blackpawn4.rect)
    screen.blit(blackpawn5.surface,blackpawn5.rect)
    screen.blit(blackpawn6.surface,blackpawn6.rect)
    screen.blit(blackpawn7.surface,blackpawn7.rect)
    screen.blit(blackpawn8.surface,blackpawn8.rect)
    
    
    
    
    

    
    center_pieces(whitecastle1, whitecastle2, blackcastle1, blackcastle2, whitebishop1, whitebishop2, blackbishop1, blackbishop2, whitequeen, blackqueen, whiteknight1, whiteknight2, blackknight2, blackknight1, whitepawn1,whitepawn2,whitepawn3,whitepawn4,whitepawn5,whitepawn6,whitepawn7,whitepawn8,blackpawn1, blackpawn2, blackpawn3, blackpawn4, blackpawn5,blackpawn6,blackpawn7,blackpawn8)


mouse_point = pygame.Rect(1100,1100,1,1)

def which_piece_mouse_selects():
    if white_players_turn and mouse_point.collidelist(white_pieces) != -1:
        return white_pieces[mouse_point.collidelist(white_pieces)]
    elif not white_players_turn and mouse_point.collidelist(black_pieces) != -1:
        return black_pieces[mouse_point.collidelist(black_pieces)]
    
def mouse_tracking(whereMouseIs):
    mouse_point.x, mouse_point.y = whereMouseIs
    pygame.draw.rect(screen, (0,0,0), mouse_point, width = 0)
    
def check_mouse_in_border(whereMouseIs):
    if board.surface.get_rect().collidepoint(whereMouseIs):
        return True
    else:
        return False

def opposite_pawn_moved_twice():
    if white_players_turn:
        for piece in black_pawns:
            if piece.justMovedTwice and piece.onBoard:
                return True, piece
    else:
        for piece in white_pawns:
                if piece.justMovedTwice and piece.onBoard:
                    return True, piece
def promote_pawn(piece):
    if white_players_turn:
        if piece.rect.collidelist(whitePawnPromotionZone) != -1:
            piece.promote_pawn()
    else:
        if piece.rect.collidelist(blackPawnPromotionZone) != -1:
            piece.promote_pawn()
        
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
                        if current_moving_piece in white_pawns or current_moving_piece in black_pawns:
                            promote_pawn(current_moving_piece)
                    
    screen.fill('white')
    whereMouseIs = pygame.mouse.get_pos()
    # Board set up
    screen.blit(board.surface, (0,0))
    DrawBoardBorder()
    put_pieces_on_board()
    
    UpdateBoard(whitecastle1)
    pygame.display.flip()
    clock.tick(60)
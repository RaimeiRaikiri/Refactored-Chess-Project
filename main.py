import pygame, sys, PieceClasses
import PieceClasses.king
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
whitequeen = PieceClasses.Queen('white',7,3, board.positionArray )
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
whiteking = PieceClasses.King('white', 7,4, board.positionArray)


# list of all white pieces
white_pieces = [whiteking,whitecastle1, whitecastle2, whitebishop1, whitebishop2, whitequeen, whiteknight1, whiteknight2, whitepawn1,whitepawn2,whitepawn3,whitepawn4,whitepawn5,whitepawn6,whitepawn7,whitepawn8]
white_pawns = [whitepawn1,whitepawn2,whitepawn3,whitepawn4,whitepawn5,whitepawn6,whitepawn7,whitepawn8]
whitePawnPromotionZone = [tile for tile in board.tileArray[0]]
whiteEnPassanteZone = [tile for tile in board.tileArray[3]]

# black pieces
blackcastle1 =  PieceClasses.Castle('black', 0,0,board.positionArray)
blackcastle2 =  PieceClasses.Castle('black', 0,7,board.positionArray)
blackbishop1 =  PieceClasses.Bishop('black', 0,2,board.positionArray)
blackbishop2 =  PieceClasses.Bishop('black', 0,5,board.positionArray)
blackqueen = PieceClasses.Queen('black', 0,3,board.positionArray)
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
blackking = PieceClasses.King('black', 0,4, board.positionArray)


# list of all black pieces 
black_pieces = [blackking,blackcastle1, blackcastle2, blackbishop1, blackbishop2, blackqueen, blackknight1, blackknight2, blackpawn1, blackpawn2, blackpawn3, blackpawn4, blackpawn5,blackpawn6,blackpawn7,blackpawn8]
black_pawns = [blackpawn1, blackpawn2, blackpawn3, blackpawn4, blackpawn5,blackpawn6,blackpawn7,blackpawn8]
blackPawnPromotionZone = [tile for tile in board.tileArray[7]]
blackEnPassanteZone = [tile for tile in board.tileArray[4]]

list_of_pieces = black_pieces + white_pieces

# For O(1) look up time of indexs of each tile rather than iterating over an 2D list each time 
tile_index = {
    '0' : (0,0), '1' : (0,1), '2' :  (0,2), '3' : (0,3), '4' : (0,4), '5' : (0,5), '6' : (0,6), '7' : (0,7),
    '8' : (1,0), '9' : (1,1), '10' : (1,2), '11' : (1,3), '12' : (1,4), '13' : (1,5), '14' : (1,6), '15' : (1,7),
    '16' : (2,0), '17' : (2,1), '18' : (2,2), '19' : (2,3), '20' : (2,4), '21' : (2,5), '22' : (2,6), '23' : (2,7),
    '24' : (3,0), '25' : (3,1), '26' : (3,2), '27' : (3,3), '28' : (3,4), '29' : (3,5), '30' : (3,6), '31' : (3,7),
    '32' : (4,0), '33' : (4,1), '34' : (4,2), '35' : (4,3), '36' : (4,4), '37' : (4,5), '38' : (4,6), '39' : (4,7),
    '40' : (5,0), '41' : (5,1), '42' : (5,2), '43' : (5,3), '44' : (5,4), '45' : (5,5), '46' : (5,6),'47' : (5,7),
    '48' : (6,0), '49' : (6,1), '50' : (6,2), '51' : (6,3), '52' : (6,4), '53' : (6,5), '54' : (6,6), '55' : (6,7),
    '56' : (7,0), '57' : (7,1), '58' : (7,2), '59' : (7,3), '60' : (7,4), '61' : (7,5), '62' : (7,6), '63' : (7,7),   
}

def DrawBoardBorder():
    # Draws a rect border around the board to prevent the pieces from leaving the board
    pygame.draw.rect(screen, (0,0,0), board.surface.get_rect(), width = 2)
    
# Updates the position array for every piece after every turn so the correct moves can be decided
def UpdateBoard(pieces: list):
    for piece in pieces:
        piece.board = board.positionArray

# Can take any number of chess pieces and center them in the tile they're on
def center_pieces(*pieces):
    for piece in pieces:
        if piece.rect.collidelist(collisionlist) != -1:
            piece.rect.center = collisionlist[piece.rect.collidelist(collisionlist)].center 

# Puts all pieces on the board, removes them if the piece has been taken
def pieces_on_board(pieces: list):
    for piece in pieces:
            screen.blit(piece.surface, piece.rect)
            center_pieces(piece)
            
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

def handle_collisions(current_piece):
    if white_players_turn:
        if current_piece.rect.collidelist(black_pieces) != -1:
            # If collided with remove from gameloop and list of pieces
            collided_piece = black_pieces[current_piece.rect.collidelist(black_pieces)]
            list_of_pieces.remove(collided_piece)
            
    else:
        if current_piece.rect.collidelist(white_pieces) != -1:
            # If collided with remove from gameloop and list of pieces
            collided_piece = white_pieces[current_piece.rect.collidelist(white_pieces)]
            list_of_pieces.remove(collided_piece)

def piece_can_move_here(piece):
    tile, tiles_index = where_piece_tries_to_move()
    piece_potential_moves = None
    if (piece in white_pawns or piece in black_pawns ) and piece.in_passante_zone:
        if piece.en_passante(piece_that_moved_last):
            piece_potential_moves = piece.get_moves() + piece.en_passante(piece_that_moved_last)
        else:
            piece_potential_moves = piece.get_moves()
    else:
        piece_potential_moves = piece.get_moves()
        
    if piece_potential_moves:
        for move in piece_potential_moves:
            if move == tiles_index:
                return tiles_index
    

def where_piece_tries_to_move():
    if mouse_point.collidelist(collisionlist) != -1:
        return collisionlist[mouse_point.collidelist(collisionlist)], tile_index[f'{mouse_point.collidelist(collisionlist)}']
    
def piece_moved(moved_piece, tile_index):
    if tile_index:
        # Save info from piece
        piece_index = (moved_piece.indexI,moved_piece.indexJ)
        piece_number = board.positionArray[piece_index[0]][piece_index[1]]
        # Make changes to the board
        board.positionArray[piece_index[0]][piece_index[1]] = 0
        board.positionArray[tile_index[0]][tile_index[1]] = piece_number
        # Make changes to info of piece
        moved_piece.indexI, moved_piece.indexJ = tile_index
        return True

def in_passante_zone(pawn):
    if white_players_turn:
        if pawn.rect.collidelist(whiteEnPassanteZone) != -1:
            pawn.in_passante_zone = True
        else:
            pawn.in_passante_zone = False
    else:
        if pawn.rect.collisionlist(blackEnPassanteZone) != -1:
            pawn.in_passante_zone = True
        else:
            pawn.in_passante_zone = False
    
game_over = False
# If not white players turn it is black players
white_players_turn = True
current_moving_piece = None
piece_that_moved_last = None
white_pawn_En_Passante = False
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
                    mouse_tracking(whereMouseIs)
                    if current_moving_piece:
                        if piece_moved(current_moving_piece, piece_can_move_here(current_moving_piece)):
                            current_moving_piece.rect.topleft = whereMouseIs
                            center_pieces(current_moving_piece)
                            handle_collisions(current_moving_piece)
                            
                            piece_that_moved_last = current_moving_piece
                            if current_moving_piece in white_pawns or current_moving_piece in black_pawns:
                                promote_pawn(current_moving_piece)
                                in_passante_zone(current_moving_piece)
                            
                            UpdateBoard(list_of_pieces)
                    
    screen.fill('white')
    whereMouseIs = pygame.mouse.get_pos()
    # Board set up
    screen.blit(board.surface, (0,0))
    DrawBoardBorder()
    pieces_on_board(list_of_pieces)
    

    pygame.display.flip()
    clock.tick(60)
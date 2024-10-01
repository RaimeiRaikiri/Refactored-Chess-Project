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
    pygame.draw.rect(screen, (0,0,0), board.surface.get_rect(topleft=(200,80)), width = 2)
    
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
    if board.surface.get_rect(topleft=(200,80)).collidepoint(whereMouseIs):
        return True
    else:
        return False
                
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
            black_pieces.remove(collided_piece)
            
    else:
        if current_piece.rect.collidelist(white_pieces) != -1:
            # If collided with remove from gameloop and list of pieces
            collided_piece = white_pieces[current_piece.rect.collidelist(white_pieces)]
            list_of_pieces.remove(collided_piece)
            white_pieces.remove(collided_piece)

def piece_can_move_here(piece):
    tile, tiles_index = where_piece_tries_to_move()
    piece_potential_moves = None
    possible_passante = False
    # If a pawn and in the en passante zone, check for en passante possible moves
    if (piece in white_pawns or piece in black_pawns ) and piece.in_passante_zone:
        possible_passante = True
        passante_move = piece.en_passante(piece_that_moved_last)
        if passante_move: # If en passante moves exist
            piece_potential_moves = piece.get_moves() + passante_move
        else:
            piece_potential_moves = piece.get_moves()
    elif piece == whiteking:
            piece_potential_moves =  piece.get_moves(whitecastle1,whitecastle2, opposition_moves())
    elif piece == blackking:
            piece_potential_moves =  piece.get_moves(blackcastle1,blackcastle2, opposition_moves())
    else:
        piece_potential_moves = piece.get_moves()
        
    if piece_potential_moves:
        for move in piece_potential_moves:
            if move == tiles_index:
                return tiles_index, tile
    

def where_piece_tries_to_move():
    if mouse_point.collidelist(collisionlist) != -1:
        return collisionlist[mouse_point.collidelist(collisionlist)], tile_index[f'{mouse_point.collidelist(collisionlist)}']
    
def piece_moved(moved_piece, tile_index, tile):
    if tile_index:
        if simulate_move_for_check_restriction(moved_piece, tile_index, tile):
            if moved_piece == whiteking:
                if whiteking.moved == False:
                    if (tile_index[0] == 7 and tile_index[1] == 2):
                        move_piece(moved_piece, tile_index, tile)
                        board.positionArray[whitecastle1.indexI][whitecastle1.indexJ] = 0
                        board.positionArray[7][3] = 2 
                        whitecastle1.rect.topleft = board.tileArray[7][3].center
                        center_pieces(whitecastle1)
                        whiteking.moved = True
                        whitecastle1.moved = True
                    elif (tile_index[0] == 7 and tile_index[1] == 6):
                        move_piece(moved_piece, tile_index, tile)
                        board.positionArray[whitecastle2.indexI][whitecastle2.indexJ] = 0
                        board.positionArray[7][5] = 2 
                        whitecastle2.rect.topleft = board.tileArray[7][5].center
                        center_pieces(whitecastle2)
                        whiteking.moved = True
                        whitecastle2.moved = True
                    else:
                        move_piece(moved_piece, tile_index, tile)    
                else:
                        move_piece(moved_piece, tile_index, tile)        
            elif moved_piece == blackking:
                if blackking.moved == False:
                    if (tile_index[0] == 0 and tile_index[1] == 2):
                        move_piece(moved_piece, tile_index, tile)
                        board.positionArray[blackcastle1.indexI][blackcastle1.indexJ] = 0
                        board.positionArray[0][3] = 2 
                        blackcastle1.rect.topleft = board.tileArray[0][3].center
                        center_pieces(blackcastle1)
                        blackking.moved = True
                        blackcastle1.moved = True
                    elif (tile_index[0] == 0 and tile_index[1] == 6):
                        move_piece(moved_piece, tile_index, tile)
                        board.positionArray[blackcastle2.indexI][blackcastle2.indexJ] = 0
                        board.positionArray[0][5] = 2 
                        blackcastle2.rect.topleft = board.tileArray[0][5].center
                        center_pieces(blackcastle2)
                        blackking.moved = True
                        blackcastle2.moved = True
                    else:
                        move_piece(moved_piece, tile_index, tile)
                else:
                    move_piece(moved_piece, tile_index, tile)
            elif moved_piece in black_pawns or moved_piece in white_pawns:
                if (moved_piece in white_pawns or moved_piece in black_pawns ) and moved_piece.in_passante_zone:
                    board.positionArray[piece_that_moved_last.indexI][piece_that_moved_last.indexJ] == 0
                    list_of_pieces.remove(piece_that_moved_last)
                    move_piece(moved_piece, tile_index, tile)
                else:
                    move_piece(moved_piece, tile_index, tile)
            else:
                move_piece(moved_piece, tile_index, tile)
                
            return True

def move_piece(moved_piece, tile_index, tile):
    # Save info from piece
    piece_index = (moved_piece.indexI,moved_piece.indexJ)
    piece_number = board.positionArray[piece_index[0]][piece_index[1]]
    # Make changes to the board
    board.positionArray[piece_index[0]][piece_index[1]] = 0
    board.positionArray[tile_index[0]][tile_index[1]] = piece_number
    # Make changes to info of piece
    moved_piece.indexI, moved_piece.indexJ = tile_index
            
def simulate_move_for_check_restriction(moved_piece, tile_index, tile):

        # Save info from piece
        piece_index = (moved_piece.indexI,moved_piece.indexJ)
        piece_number = board.positionArray[piece_index[0]][piece_index[1]]
        # Make changes to the board
        board.positionArray[piece_index[0]][piece_index[1]] = 0
        previous_tile_state = board.positionArray[tile_index[0]][tile_index[1]]
        
        displaced_piece = None
        if tile.collidelist(list_of_pieces) != -1:
            displaced_piece = list_of_pieces[tile.collidelist(list_of_pieces)]
        if displaced_piece:
            if displaced_piece.color == 'white':
                white_pieces.remove(displaced_piece)
            else:
                black_pieces.remove(displaced_piece)
    
        board.positionArray[tile_index[0]][tile_index[1]] = piece_number
        # Make changes to info of piece
        moved_piece.indexI, moved_piece.indexJ = tile_index
        checked = check()
        
        # Revert changes to piece and board
        moved_piece.indexI, moved_piece.indexJ = piece_index
        if displaced_piece:
            if displaced_piece.color == 'white':
                white_pieces.append(displaced_piece)
            else:
                black_pieces.append(displaced_piece)
                
        board.positionArray[piece_index[0]][piece_index[1]] = piece_number
        board.positionArray[tile_index[0]][tile_index[1]] = previous_tile_state
        
        # Check if that move would result in check
        if white_players_turn and checked == 'white':
            return False
        elif not white_players_turn and checked == 'black':
            return False
        else:
            return True
        
def in_passante_zone(pawn):
    if white_players_turn:
        if pawn.rect.collidelist(whiteEnPassanteZone) != -1:
            pawn.in_passante_zone = True
        else:
            pawn.in_passante_zone = False
    else:
        if pawn.rect.collidelist(blackEnPassanteZone) != -1:
            pawn.in_passante_zone = True
        else:
            pawn.in_passante_zone = False

def check():
    if white_players_turn:
        moves = []
        for piece in black_pieces:
            if piece == blackking:
                continue
            pieceMoves = piece.get_moves()
            if pieceMoves:
                moves += pieceMoves
        if (whiteking.indexI, whiteking.indexJ) in moves:
            return 'white'
    else:
        moves = []
        for piece in white_pieces:
            if piece == whiteking:
                continue
            pieceMoves = piece.get_moves()
            if pieceMoves:
                moves += pieceMoves
        if (blackking.indexI, blackking.indexJ) in moves:
            return 'black'

def in_checkmate():
    if white_players_turn:
        moves = []
        for piece in white_pieces:
            possible_passante = False
            # If a pawn and in the en passante zone, check for en passante possible moves
            if (piece in white_pawns ) and piece.in_passante_zone:
                possible_passante = True
                passante_move = piece.en_passante(piece_that_moved_last)
                if passante_move: # If en passante moves exist
                    moves = piece.get_moves() + passante_move
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
                else:
                    moves = piece.get_moves()
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            elif piece == whiteking:
                moves = piece.get_moves(whitecastle1,whitecastle2, opposition_moves())
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            else:
                moves = piece.get_moves()
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False

        return True
    else:
        moves = []
        for piece in black_pieces:
            possible_passante = False
            # If a pawn and in the en passante zone, check for en passante possible moves
            if (piece in black_pawns) and piece.in_passante_zone:
                possible_passante = True
                passante_move = piece.en_passante(piece_that_moved_last)
                if passante_move: # If en passante moves exist
                    moves = piece.get_moves() + passante_move
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
                else:
                    moves = piece.get_moves()
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            elif piece == blackking:
                moves = piece.get_moves(blackcastle1,blackcastle2, opposition_moves())
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            else:
                moves = piece.get_moves()
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False

        return True

def in_stalemate():
    if white_players_turn and not white_in_check:
        moves = []
        for piece in white_pieces:
            possible_passante = False
            # If a pawn and in the en passante zone, check for en passante possible moves
            if (piece in white_pawns ) and piece.in_passante_zone:
                possible_passante = True
                passante_move = piece.en_passante(piece_that_moved_last)
                if passante_move: # If en passante moves exist
                    moves = piece.get_moves() + passante_move
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
                else:
                    moves = piece.get_moves()
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            elif piece == whiteking:
                moves = piece.get_moves(whitecastle1,whitecastle2, opposition_moves())
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            else:
                moves = piece.get_moves()
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False

        return True
    
    elif not white_players_turn and not black_in_check:
        moves = []
        for piece in black_pieces:
            possible_passante = False
            # If a pawn and in the en passante zone, check for en passante possible moves
            if (piece in black_pawns) and piece.in_passante_zone:
                possible_passante = True
                passante_move = piece.en_passante(piece_that_moved_last)
                if passante_move: # If en passante moves exist
                    moves = piece.get_moves() + passante_move
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
                else:
                    moves = piece.get_moves()
                    for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            elif piece == blackking:
                moves = piece.get_moves(blackcastle1,blackcastle2, opposition_moves())
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False
            else:
                moves = piece.get_moves()
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False

        return True

def opposition_moves():
    if white_players_turn:
        moves = []
        for piece in black_pieces:
            possible_passante = False
            # If a pawn and in the en passante zone, check for en passante possible moves
            if (piece in black_pawns) and piece.in_passante_zone:
                possible_passante = True
                passante_move = piece.en_passante(piece_that_moved_last)
                if passante_move: # If en passante moves exist
                    moves += piece.get_moves() + passante_move
                else:
                    moves = piece.get_moves()
            elif piece == blackking:
                moves += piece.get_moves(blackcastle1,blackcastle2, (-1,-1))
            else:
                moves += piece.get_moves()

        return moves
    else:
        moves = []
        for piece in white_pieces:
            possible_passante = False
            # If a pawn and in the en passante zone, check for en passante possible moves
            if (piece in white_pawns ) and piece.in_passante_zone:
                possible_passante = True
                passante_move = piece.en_passante(piece_that_moved_last)
                if passante_move: # If en passante moves exist
                    moves += piece.get_moves() + passante_move
                else:
                    moves += piece.get_moves()
            elif piece == whiteking:
                moves += piece.get_moves(whitecastle1,whitecastle2, (-1,-1))
            else:
                moves += piece.get_moves()

        return moves
        
def coordinate_indicators():
    screen.blit(gameFont.render('a',True, 'black'), (240,882))
    screen.blit(gameFont.render('b',True, 'black'), (340,882))
    screen.blit(gameFont.render('c',True, 'black'), (440,882))
    screen.blit(gameFont.render('d',True, 'black'), (540,882))
    screen.blit(gameFont.render('e',True, 'black'), (640,882))
    screen.blit(gameFont.render('f',True, 'black'), (740,882))
    screen.blit(gameFont.render('g',True, 'black'), (840,882))
    screen.blit(gameFont.render('h',True, 'black'), (940,882))
    
    screen.blit(gameFont.render('1',True, 'black'), (160,820))
    screen.blit(gameFont.render('2',True, 'black'), (160,720))
    screen.blit(gameFont.render('3',True, 'black'), (160,620))
    screen.blit(gameFont.render('4',True, 'black'), (160,520))
    screen.blit(gameFont.render('5',True, 'black'), (160,420))
    screen.blit(gameFont.render('6',True, 'black'), (160,320))
    screen.blit(gameFont.render('7',True, 'black'), (160,220))
    screen.blit(gameFont.render('8',True, 'black'), (160,120))
    
game_over = False
# If not white players turn it is black players
white_players_turn = True
current_moving_piece = None
piece_that_moved_last = None
gameFont = pygame.font.Font("freesansbold.ttf", 32)
white_in_check = False
black_in_check = False

white_wins = False
black_wins = False
Draw = False

quit_rect_on_screen = pygame.Rect(550,550,100,50)

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_rect_on_screen.collidepoint(whereMouseIs):
                        pygame.quit()
                        sys.exit()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Track mouse location on button down
                    mouse_tracking(whereMouseIs)
                    current_moving_piece = which_piece_mouse_selects()
                    
                if event.type == pygame.MOUSEBUTTONUP and check_mouse_in_border(whereMouseIs):
                    # Track mouse location on button up
                    mouse_tracking(whereMouseIs)
                    if current_moving_piece:
                        # Checks if piece has moved / can move
                        
                        # Prevents impossible attempt to unpack a None type
                        tile_position, tile_rect = None, None
                        if piece_can_move_here(current_moving_piece):
                            tile_position, tile_rect = piece_can_move_here(current_moving_piece)
                        
                        if piece_moved(current_moving_piece, tile_position, tile_rect):
                            # if its moved, move sprite, center it and handle any collisions
                            current_moving_piece.rect.topleft = whereMouseIs
                            center_pieces(current_moving_piece)
                            handle_collisions(current_moving_piece)
                            
                            # update last moved piece for possible enpassante, other pawn specific checks
                            piece_that_moved_last = current_moving_piece
                            if current_moving_piece in white_pawns or current_moving_piece in black_pawns:
                                promote_pawn(current_moving_piece)
                                in_passante_zone(current_moving_piece)
                                if current_moving_piece.moved == False:
                                    current_moving_piece.moved = True
                            
                            # Switch turn and update board
                            if white_players_turn:
                                white_players_turn = False
                            else:
                                white_players_turn = True
                                
                            UpdateBoard(list_of_pieces)
                            
                            if check() == 'white':
                                white_in_check = True
                            else:
                                white_in_check = False
                            
                            if check() == 'black':
                                black_in_check = True
                            else:
                                black_in_check = False
                            
                            if white_players_turn and white_in_check:
                                if in_checkmate():
                                    black_wins = True
                                    game_over = True
                            elif not white_players_turn and black_in_check:
                                if in_checkmate():
                                    white_wins = True
                                    game_over = True
                                    
                            if white_players_turn and not white_in_check:
                                if in_stalemate():
                                    Draw = True
                                    game_over = True
                            elif not white_players_turn and not black_in_check:
                                if in_stalemate():
                                    Draw = True
                                    game_over = True
                                    
                              
    screen.fill('white')
    whereMouseIs = pygame.mouse.get_pos()
    # Board set up
    screen.blit(board.surface, (200,80))
    DrawBoardBorder()
    pieces_on_board(list_of_pieces)
    coordinate_indicators()
    if black_wins or white_wins:
        checkmate_text = gameFont.render('Checkmate', False, 'black', 'white')
        screen.blit(checkmate_text, (500,30))
    elif white_in_check:
        white_check_text = gameFont.render('white in check', False,'black','white')
        screen.blit(white_check_text, (500,30))
    elif black_in_check:
        black_check_text = gameFont.render('black in check', False,'black','white')
        screen.blit(black_check_text, (500,30))
    elif white_players_turn:
        white_turn_text =  gameFont.render('white turn', False, 'black', 'white')
        screen.blit(white_turn_text, (500,30))
    else:
        black_turn_text = gameFont.render('black turn', False, 'black', 'white')
        screen.blit(black_turn_text, (500,30))

    # So it doesn't keep creating these when no one has won yet
    if white_wins or black_wins:
        # Create surface for text and quit button to be placed
        end_game_surface = pygame.Surface((600,600))
        end_game_surface.fill('white')
        
        # Creates quit button and puts it on the end screen surface
        quit_surface = pygame.Surface((100,50))
        quit_surface.fill('white')
        if quit_rect_on_screen.collidepoint(whereMouseIs):
             game_quit_text = gameFont.render(f"Quit", False, 'red', (255,255,255))
        else:
            game_quit_text = gameFont.render(f"Quit", False, 'black', (255,255,255))
        quit_surface.blit(game_quit_text, (15,10))
        # Puts quit button on end game surface and gives it a border
        end_game_surface.blit(quit_surface, (250,350))
        quit_rect =  quit_surface.get_rect(topleft=(250,350))
        pygame.draw.rect(end_game_surface, (0,0,0), quit_rect, 2)

        if white_wins:
            # Player win text and adds to final end game surface
            white_win_text = gameFont.render('White Player Wins!', True, 'black', 'white')
            end_game_surface.blit(white_win_text,(150,200))
      
            # Puts the end game surface on the screen
            screen.blit(end_game_surface, (300,200))
            pygame.draw.rect(screen, (255,0,0), end_game_surface.get_rect(topleft=(300,200)), width = 2)
            
        if black_wins:
            # Player win text and adds to final end game surface
            black_win_text = gameFont.render('Black Player Wins!', True, 'black', 'white')
            end_game_surface.blit(black_win_text,(150,200))

            # Puts the end game surface on the screen
            screen.blit(end_game_surface, (300,200))
            pygame.draw.rect(screen, (255,0,0), end_game_surface.get_rect(topleft=(300,200)), width = 2)
            
    if Draw:
        end_game_surface = pygame.Surface((600,600))
        end_game_surface.fill('white')
        
        # Creates quit button and puts it on the end screen surface
        quit_surface = pygame.Surface((100,50))
        quit_surface.fill('white')
        if quit_rect_on_screen.collidepoint(whereMouseIs):
                game_quit_text = gameFont.render(f"Quit", False, 'red', (255,255,255))
        else:
            game_quit_text = gameFont.render(f"Quit", False, 'black', (255,255,255))
        quit_surface.blit(game_quit_text, (15,10))
        # Puts quit button on end game surface and gives it a border
        end_game_surface.blit(quit_surface, (250,350))
        quit_rect =  quit_surface.get_rect(topleft=(250,350))
        pygame.draw.rect(end_game_surface, (0,0,0), quit_rect, 2)
        
        draw_text = gameFont.render('You Draw!', True, 'black', 'white')
        end_game_surface.blit(draw_text,(220,200))
        # Puts the end game surface on the screen
        screen.blit(end_game_surface, (300,200))
        pygame.draw.rect(screen, (255,0,0), end_game_surface.get_rect(topleft=(300,200)), width = 2)
                
    pygame.display.flip()
    clock.tick(60)
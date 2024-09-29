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
    else:
        piece_potential_moves = piece.get_moves()
        
    if piece_potential_moves:
        for move in piece_potential_moves:
            if move == tiles_index:
                if possible_passante and passante_move[0] == move:
                    board.positionArray[piece_that_moved_last.indexI][piece_that_moved_last.indexJ] == 0
                    list_of_pieces.remove(piece_that_moved_last)
                return tiles_index, tile
    

def where_piece_tries_to_move():
    if mouse_point.collidelist(collisionlist) != -1:
        return collisionlist[mouse_point.collidelist(collisionlist)], tile_index[f'{mouse_point.collidelist(collisionlist)}']
    
def piece_moved(moved_piece, tile_index, tile):
    if tile_index:
        if simulate_move_for_check_restriction(moved_piece, tile_index, tile):
            # Save info from piece
            piece_index = (moved_piece.indexI,moved_piece.indexJ)
            piece_number = board.positionArray[piece_index[0]][piece_index[1]]
            # Make changes to the board
            board.positionArray[piece_index[0]][piece_index[1]] = 0
            board.positionArray[tile_index[0]][tile_index[1]] = piece_number
            # Make changes to info of piece
            moved_piece.indexI, moved_piece.indexJ = tile_index
                
            return True

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
            pieceMoves = piece.get_moves()
            if pieceMoves:
                moves += pieceMoves
        if (whiteking.indexI, whiteking.indexJ) in moves:
            return 'white'
    else:
        moves = []
        for piece in white_pieces:
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
            else:
                moves = piece.get_moves()
                for move in moves:
                        if simulate_move_for_check_restriction(piece, move, board.tileArray[move[0]][move[1]]):
                            return False

        return True
    
            


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

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over:
                pass
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
                                    
                              
                                
                    
    screen.fill('white')
    whereMouseIs = pygame.mouse.get_pos()
    # Board set up
    screen.blit(board.surface, (0,0))
    DrawBoardBorder()
    pieces_on_board(list_of_pieces)
    if black_wins or white_wins:
        checkmate_text = gameFont.render('Checkmate', False, 'black', 'white')
        screen.blit(checkmate_text, (900,800))
    elif white_in_check:
        white_check_text = gameFont.render('white in check', False,'black','white')
        screen.blit(white_check_text, (900,800))
    elif black_in_check:
        black_check_text = gameFont.render('black in check', False,'black','white')
        screen.blit(black_check_text, (900,800))
    elif white_players_turn:
        white_turn_text =  gameFont.render('white turn', False, 'black', 'white')
        screen.blit(white_turn_text, (900,200))
    else:
        black_turn_text = gameFont.render('black turn', False, 'black', 'white')
        screen.blit(black_turn_text, (900,200))

    pygame.display.flip()
    clock.tick(60)
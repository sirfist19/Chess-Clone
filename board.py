from essential_fxns import *
import copy

class Board:
    def __init__(self):
        self.empty_char = "."
        self.content = [[self.empty_char for i in range(8)] for j in range(8)]
        self.pieces = [[[] for i in range(8)] for j in range(8)] #keeps track of all the pieces, if a cell is empty then this is empty, if it has a piece then it is stored here
        self.square_is_attacked = [[0 for i in range(8)] for j in range(8)] #0 for not attacked, 1 for attacked by white, 2 for attacked by black, 3 for attacked by both
        self.white_turn = True
        self.game_over = False

    def display(self):
        print("========================================")
        print("Text Based Chess Game")
        print("========================================")
        for line in self.content:
            to_print = "                "
            for square in line:
                to_print += square
            print(to_print)
        
        print("========================================")

    def set_square_empty(self, coord):
        self.content[coord[1]][coord[0]] = self.empty_char
        self.pieces[coord[1]][coord[0]] = []

    def check_game_over(self):
        #checks for checkmates
        #only need to check the current player's King
        
        white_king = self.get_king_white()
        black_king = self.get_king_black()
        black_wins = self.check_checkmate(white_king)
        white_wins = self.check_checkmate(black_king)

        if black_wins:
            print("Black Wins!")
        if white_wins:
            print("White wins!")

        return (black_wins or white_wins)
        

    def check_checkmate(self, king): #check if the passed in king is checkmated
        king_is_white = (king.color == "white")

        #the king is in check
        if not self.king_in_check(king):
            return False

        #check to see if the king can move to other squares
        for square in king.influence:
            square_status = self.square_is_attacked[square[1]][square[0]]
            piece_on_square = self.pieces[square[1]][square[0]]

            #if the square is occupied by the piece of the same color, then the king cannot move to that square
            if king_is_white and piece_on_square and piece_on_square.color == "white":
                continue
            if not king_is_white and piece_on_square and piece_on_square.color == "black":
                continue

            #if the king is white and the square is only attacked by white or not attacked the king can move here
            if king_is_white and (square_status == 0 or square_status == 1): 
                return False
            if not king_is_white and (square_status == 0 or square_status == 2):
                return False

        return True

    def king_in_check(self, king):
        king_is_white = (king.color == "white")

        #check to see if the current square the king is on is attacked by the opponent
        square_status = self.square_is_attacked[king.coord[1]][king.coord[0]]
        if king_is_white and (square_status == 0 or square_status == 1): #only attacked by white or not attacked -> so not in check
            return False
        if not king_is_white and (square_status == 0 or square_status == 2):
            return False
        return True

    def get_king_white(self):
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if not piece:
                    continue
                if piece.name == "King" and piece.color == "white":
                    return piece
    def get_king_black(self):
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if not piece:
                    continue
                if piece.name == "King" and piece.color == "black":
                    return piece
        
    def set_square_with_piece(self, piece, des_coord):
        self.content[des_coord[1]][des_coord[0]] = piece.value
        self.pieces[des_coord[1]][des_coord[0]] = piece

    def piece_is_blocking_move(self, squares_to_check): 
        #checks to see if any of the squares that are passed in are occupied
        #if so, returns true
        #else returns false
        if not squares_to_check: #no squares to check so there is no piece blocking
            print("Error squares to check is empty")
            return False

        for square in squares_to_check:
            if self.pieces[square[1]][square[0]] and self.pieces[square[1]][square[0]].name != "King": #if the king is blocking then the influence can still go past him
                return True
        return False
        
    def add_piece(self, piece_to_add, des_coord):
        self.set_square_with_piece(piece_to_add, des_coord)
        
    def add_pieces(self, pieces_to_add): #used to setup a board at the start
        for piece in pieces_to_add:
           self.add_piece(piece, piece.coord)

    def update_all_pieces_influence(self):
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if not piece:
                    continue
                
                piece.set_influence()
                #print(piece.influence)
                self.set_piece_influence_square_blocking(piece)
                #print(piece.influence)

    def display_all_pieces_influence(self):
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if not piece:
                    continue
                print(piece.influence)

    def display_all_pieces_protected(self):
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if not piece:
                    continue
                print(piece)
                print(piece.protected)

    def display_all_square_attack_status(self):
        for row in self.square_is_attacked:
            print(row)
        #print(self.square_is_attacked)

    def apply_move(self, piece, des_square): #move a piece
        self.set_square_empty(piece.coord)
        self.set_square_with_piece(piece, des_square)
        piece.coord = des_square

        piece.has_moved = True

        #update the influence of all the pieces
        self.update_all_pieces_influence()

        #update the attacked squares and protected pieces
        self.update_attack_and_protect_status()

        

    def get_matching_pieces(self, type_of_piece_to_move, des_square):
        res = []
        for i in range(0, 8):
            for j in range(0, 8):
                piece_to_check = self.pieces[i][j]
                #print(piece_to_check)
                if not piece_to_check: #square is empty
                    continue
                elif piece_to_check.name != type_of_piece_to_move:#has to match the piece type
                    continue
                elif (self.white_turn and piece_to_check.color == "Black") or (not self.white_turn and piece_to_check.color == "White"):
                    continue
                else: 
                    #check whether the piece can move to the des_square
                    if self.move_is_valid(piece_to_check.coord, des_square):
                        res.append(piece_to_check)
        return res
    
    def set_piece_influence_square_blocking(self, piece):
        new_influence = []
        for des_square in piece.influence:
            #for each of the possible square's within a piece's influence,
            #   check to see if a piece is blocking that square from really being in that pieces influence
            squares_to_check = piece.piece_is_blocking(des_square) #gets the squares to the des_square for the given piece
            if not self.piece_is_blocking_move(squares_to_check):
                new_influence.append(des_square)
        piece.influence = new_influence

    def update_attack_and_protect_status(self):
        #reset the attacking array
        self.square_is_attacked = [[0 for i in range(8)] for j in range(8)]

        #go through each piece and check what it is attacking -> need a fxn for this!
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if not piece:
                    continue

                #for each piece, update all squares it is currently attacking
                for square in piece.influence:
                    self.update_square_attack_status(square, piece.color)

        #now the self.square_is_attacked is fully updated
        #UPDATE THE protected ATTRIBUTE OF EACH PIECE
        for i in range(8):
            for j in range(8):
                piece = self.pieces[i][j]
                if not piece:
                    continue

                cur_attack_status = self.square_is_attacked[i][j]
                if cur_attack_status == 0:
                    piece.protected = False
                if (cur_attack_status == 1 and piece.color == "white") or (cur_attack_status == 2 and piece.color == "black") or (cur_attack_status == 3):
                    piece.protected = True

    def update_square_attack_status(self, square, attacking_piece_color): #given a square and the color of a piece that is attacking it, update that square to reflect that the piece is attacking it
        cur_status = self.square_is_attacked[square[1]][square[0]]
        new_status = cur_status
        if cur_status == 0:
           
            if attacking_piece_color == "white":
                new_status = 1
            elif attacking_piece_color == "black":
                new_status = 2
        elif cur_status == 1:
            if attacking_piece_color == "black":
                new_status = 3
        elif cur_status == 2:
            if attacking_piece_color == "white":
                new_status = 3
        self.square_is_attacked[square[1]][square[0]] = new_status

    def move_is_valid(self, piece_square, des_square):
        piece_to_move = self.pieces[piece_square[1]][piece_square[0]]
        piece_already_on_des_square = self.pieces[des_square[1]][des_square[0]]

        #try to move an empty square
        if not piece_to_move:
            print("There is no piece on that square.")
            return False
        #ensure that the player whose turn it is moves one of their own pieces
        if (self.white_turn and piece_to_move.color == "black") or (not self.white_turn and piece_to_move.color == "white"):
            print("You cannot move one of your opponent's pieces.")
            return False

        #trying to move to a square with one of your own pieces already on it
        if (piece_already_on_des_square #there is a piece on the new square
            and 
            piece_already_on_des_square.color == piece_to_move.color #it is your own piece
            ):
            print("You can't go onto a square that already has one of your pieces.")
            return False

        #trying to capture the King
        if (piece_already_on_des_square 
            and
            piece_already_on_des_square.name == "King"
            ):
            print("You cannot capture the King.")
            return False

        #if the current player's king is in check, 
        #       ensure that the piece being moved is the King
        if self.white_turn:
            king = self.get_king_white()
        else:
            king = self.get_king_black()
        in_check = self.king_in_check(king)
        if in_check and piece_to_move.name != "King":
            print("If your King is in check, then you must move your King out of check")
            return False

        #check about capturing
        is_capturing = self.capture(piece_already_on_des_square)
        squares_to_check = []

        #check the piece itself to see if it is a valid move
        if piece_to_move.name == "Pawn":
            valid_move = piece_to_move.move(des_square, is_capturing)
        else:
            valid_move = piece_to_move.move(des_square)
        
        #if the piece is a king check to make sure des_square isn't already attacked by the enemy
        if piece_to_move.name == "King":
            des_square_status = self.square_is_attacked[des_square[1]][des_square[0]]
            if des_square_status == 3 or (piece_to_move.color == "white" and des_square_status == 2) or (piece_to_move.color == "black" and des_square_status == 1):
                print("You cannot move the King onto a square attacked by the enemy")
                return False

        if piece_to_move.name != "Pawn" and piece_to_move.name != "Knight" and piece_to_move.name != "King":
            squares_to_check = piece_to_move.piece_is_blocking(des_square)

        #check to see if the piece trying to be moved is pinned
        #this check comes last because this needs to be a valid move asides from a 
        #   possible pin
        
        if self.is_pinned(piece_to_move, des_square):
            return False

        if not squares_to_check:
            return valid_move
            
        #checking for a piece being in the way of the move
        if self.piece_is_blocking_move(squares_to_check):
            print("A piece is blocking that move from happening.")
            return False

        return valid_move

    def is_pinned(self, piece_to_move, des_square):
        #emulate the board if the move was made
        #on this new board check to see if the player that just moved's king is in check
        #if so then return true, else return false

        #copy the board to try the move on
        copy_board = copy.deepcopy(self)

        #get the equivalent of piece_to_move on the new board
        piece_to_move = copy_board.pieces[piece_to_move.coord[1]][piece_to_move.coord[0]]
        is_white = (piece_to_move.color == "white")
        
        #try the move on copy_board
        copy_board.apply_move(piece_to_move, des_square)

        #check the board and see if by moving the piece the player exposed their king
        if is_white:
            king = copy_board.get_king_white()
            king_status = copy_board.square_is_attacked[king.coord[1]][king.coord[0]]
            if king_status == 2 or king_status == 3: #attacked by black
                print("The piece to move is pinned.")
                return True
        else:
            king = copy_board.get_king_black()
            king_status = copy_board.square_is_attacked[king.coord[1]][king.coord[0]]
            if king_status == 1 or king_status == 3: #attacked by white
                print("The piece to move is pinned.")
                return True
        return False

    def kingside_castling(self):
        if self.white_turn:
            king = self.get_king_white()
            kingside_rook = self.pieces[7][7] #the rook at h1
            
            if (
                #the king hasn't moved and is on the right square
                king.has_moved == False 
                and king.coord == chess_notation_to_board_square("e1")
           
                and kingside_rook #the rook is not null

                #the rook is the correct piece
                and kingside_rook.color == "white" 
                and kingside_rook.name == "Rook" 

                #the rook hasn't moved and is on the right square
                and kingside_rook.has_moved == False
                and kingside_rook.coord == chess_notation_to_board_square("h1")

                #squares e1, f1, and g1 are not attacked
                and (self.square_is_attacked[7][4] == 0 or self.square_is_attacked[7][4] == 1) #e1
                and (self.square_is_attacked[7][5] == 0 or self.square_is_attacked[7][5] == 1) #f1
                and (self.square_is_attacked[7][6] == 0 or self.square_is_attacked[7][6] == 1) #g1

                #squares f1 and g1 are not occupied
                and not self.pieces[7][5]
                and not self.pieces[7][6]
            ):
                #actually castle!
                self.apply_move(king, [6, 7]) #king goes to f1
                self.apply_move(kingside_rook, [5, 7]) #rook goes to g1
                self.white_turn = not self.white_turn #change the turns
            else:
                print("Not a valid castle move")

        else:
            king = self.get_king_black()
            kingside_rook = self.pieces[0][7] #the rook at h8
            
            if (
                #the king hasn't moved and is on the right square
                king.has_moved == False 
                and king.coord == chess_notation_to_board_square("e8")
           
                and kingside_rook #the rook is not null

                #the rook is the correct piece
                and kingside_rook.color == "black" 
                and kingside_rook.name == "Rook" 

                #the rook hasn't moved and is on the right square
                and kingside_rook.has_moved == False
                and kingside_rook.coord == chess_notation_to_board_square("h8")

                #squares e8, f8, and g8 are not attacked
                and (self.square_is_attacked[0][4] == 0 or self.square_is_attacked[0][4] == 2) #e8
                and (self.square_is_attacked[0][5] == 0 or self.square_is_attacked[0][5] == 2) #f8
                and (self.square_is_attacked[0][6] == 0 or self.square_is_attacked[0][6] == 2) #g8

                #squares f8 and g8 are not occupied
                and not self.pieces[0][5]
                and not self.pieces[0][6]
            ):
                #actually castle!
                self.apply_move(king, [6, 0]) #king goes to f1
                self.apply_move(kingside_rook, [5, 0]) #rook goes to g1
                self.white_turn = not self.white_turn #change the turns
            else:
                print("Not a valid castle move")

    def queenside_castling(self):
        if self.white_turn:
            king = self.get_king_white()
            queenside_rook = self.pieces[7][0] #the rook at a1
            
            if (
                #the king hasn't moved and is on the right square
                king.has_moved == False 
                and king.coord == chess_notation_to_board_square("e1")
           
                and queenside_rook #the rook is not null

                #the rook is the correct piece
                and queenside_rook.color == "white" 
                and queenside_rook.name == "Rook" 

                #the rook hasn't moved and is on the right square
                and queenside_rook.has_moved == False
                and queenside_rook.coord == chess_notation_to_board_square("a1")

                #squares e1, d1, and c1 are not attacked
                and (self.square_is_attacked[7][4] == 0 or self.square_is_attacked[7][4] == 1) #e1
                and (self.square_is_attacked[7][3] == 0 or self.square_is_attacked[7][3] == 1) #d1
                and (self.square_is_attacked[7][2] == 0 or self.square_is_attacked[7][2] == 1) #c1

                #squares b1, c1, and d1 are not occupied
                and not self.pieces[7][1]
                and not self.pieces[7][2]
                and not self.pieces[7][3]
            ):
                #actually castle!
                self.apply_move(king, [2, 7]) #king goes to c1
                self.apply_move(queenside_rook, [3, 7]) #rook goes to d1
                self.white_turn = not self.white_turn #change the turns
            else:
                print("Not a valid castle move")

        else:
            king = self.get_king_black()
            queenside_rook = self.pieces[0][0] #the rook at a8
            
            if (
                #the king hasn't moved and is on the right square
                king.has_moved == False 
                and king.coord == chess_notation_to_board_square("e8")
           
                and queenside_rook #the rook is not null

                #the rook is the correct piece
                and queenside_rook.color == "black" 
                and queenside_rook.name == "Rook" 

                #the rook hasn't moved and is on the right square
                and queenside_rook.has_moved == False
                and queenside_rook.coord == chess_notation_to_board_square("a8")

                #squares e8, f8, and g8 are not attacked
                and (self.square_is_attacked[0][4] == 0 or self.square_is_attacked[0][4] == 2) #e8
                and (self.square_is_attacked[0][3] == 0 or self.square_is_attacked[0][3] == 2) #d8
                and (self.square_is_attacked[0][2] == 0 or self.square_is_attacked[0][2] == 2) #c8

                #squares b8, c8, d8 are not occupied
                and not self.pieces[0][1]
                and not self.pieces[0][2]
                and not self.pieces[0][3]
            ):
                #actually castle!
                self.apply_move(king, [2, 0]) #king goes to c8
                self.apply_move(queenside_rook, [3, 0]) #rook goes to d8
                self.white_turn = not self.white_turn #change the turns
            else:
                print("Not a valid castle move")

    def move(self, player_input): 
        if invalid_move(player_input):
            return

        processed_out = process_input(player_input)
        print(processed_out)
        if processed_out == "kingside castling":
            self.kingside_castling()
            return
        elif processed_out == "queenside castling":
            self.queenside_castling()
            return

        type_of_piece_to_move = processed_out[0]
        des_square = processed_out[1]
        
        possible_pieces_to_move = self.get_matching_pieces(
            type_of_piece_to_move,
            des_square
        )

        if not possible_pieces_to_move:
            print("No piece matches that move.")
            return
        if len(possible_pieces_to_move) > 1:
            print("More than one piece matches that move")
        
        piece_to_move = possible_pieces_to_move[0]

        #NOW ACTUALLY MOVE THE PIECE TO THE DESIRED SQUARE
            #if is_capturing:
            #    to_print = "You captured " + piece_already_on_des_square.color + "'s " + piece_already_on_des_square.name + "."
            #    print(to_print)
        self.apply_move(piece_to_move, des_square) #actually move the pieces on the board
        self.white_turn = not self.white_turn #change the turns

    def capture(self, piece_on_des_square):
        if not piece_on_des_square:
            return False
        return True



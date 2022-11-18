#this is a text based Chess game in python
from pieces import *
from essential_fxns import *
from board import Board

if __name__ == "__main__":
    board = Board()
    empty_board = []
    test_setup = [
       King("white", chess_notation_to_board_square("e4")),
       King("black", chess_notation_to_board_square("a8")),
       Pawn("white", chess_notation_to_board_square("e2")),
       Pawn("white", chess_notation_to_board_square("f2")),
       Pawn("white", chess_notation_to_board_square("g2")),
       Pawn("white", chess_notation_to_board_square("h2")),
       Pawn("black", chess_notation_to_board_square("e6")),
       Pawn("white", chess_notation_to_board_square("d6")),
       Rook("white", chess_notation_to_board_square("a1")),
       #Bishop("black", chess_notation_to_board_square("e4"))
    ]
    rook_checkmate = [
                        Rook("white", chess_notation_to_board_square("a8")),
                        Rook("white", chess_notation_to_board_square("b7")),
                        King("black", chess_notation_to_board_square("e8")),
                        King("white", chess_notation_to_board_square("e1"))
                ]
    rook_checkmate2 = [
                        Rook("black", chess_notation_to_board_square("a8")),
                        Rook("black", chess_notation_to_board_square("b7")),
                        King("white", chess_notation_to_board_square("e8")),
                        King("black", chess_notation_to_board_square("e1"))
                ]
    queen_king_checkmate1 = [
                        Queen("black", chess_notation_to_board_square("e7")),
                        King("black", chess_notation_to_board_square("e6")),
                        King("white", chess_notation_to_board_square("e8"))
                ]
    rook_endgame = [
                        Rook("white", chess_notation_to_board_square("a8")),
                        King("white", chess_notation_to_board_square("d3")),
                        King("black", chess_notation_to_board_square("d5"))

    ]
    in_check1 = [
       King("white", chess_notation_to_board_square("e1")),
       King("black", chess_notation_to_board_square("a8")),
       Pawn("white", chess_notation_to_board_square("e2")),
       Pawn("white", chess_notation_to_board_square("f2")),
       Pawn("white", chess_notation_to_board_square("g2")),
       Pawn("white", chess_notation_to_board_square("h2")),
       #Pawn("white", chess_notation_to_board_square("d2")),
       Pawn("black", chess_notation_to_board_square("e6")),
       Pawn("black", chess_notation_to_board_square("d6")),
       Rook("black", chess_notation_to_board_square("a1")),
       Bishop("black", chess_notation_to_board_square("e4"))
    ]
    kingside_castling = [
        King("white", chess_notation_to_board_square("e1")),
        Rook("white", chess_notation_to_board_square("h1")),
        King("black", chess_notation_to_board_square("e8")),
        Rook("black", chess_notation_to_board_square("h8"))
    ]
    queenside_castling = [
        King("white", chess_notation_to_board_square("e1")),
        Rook("white", chess_notation_to_board_square("a1")),
        King("black", chess_notation_to_board_square("e8")),
        Rook("black", chess_notation_to_board_square("a8"))
    ]
    standard_setup = [
                        #white
                        Rook("white", chess_notation_to_board_square("a1")),
                        Knight("white", chess_notation_to_board_square("b1")),
                        Bishop("white", chess_notation_to_board_square("c1")),
                        Queen("white", chess_notation_to_board_square("d1")),
                        King("white", chess_notation_to_board_square("e1")),
                        Bishop("white", chess_notation_to_board_square("f1")),
                        Knight("white", chess_notation_to_board_square("g1")),
                        Rook("white", chess_notation_to_board_square("h1")),
                        Pawn("white", chess_notation_to_board_square("a2")),
                        Pawn("white", chess_notation_to_board_square("b2")),
                        Pawn("white", chess_notation_to_board_square("c2")),
                        Pawn("white", chess_notation_to_board_square("d2")),
                        Pawn("white", chess_notation_to_board_square("e2")),
                        Pawn("white", chess_notation_to_board_square("f2")),
                        Pawn("white", chess_notation_to_board_square("g2")),
                        Pawn("white", chess_notation_to_board_square("h2")),
                                

                        #black
                        Rook("black", chess_notation_to_board_square("a8")),
                        Knight("black", chess_notation_to_board_square("b8")),
                        Bishop("black", chess_notation_to_board_square("c8")),
                        Queen("black", chess_notation_to_board_square("d8")),
                        King("black", chess_notation_to_board_square("e8")),
                        Bishop("black", chess_notation_to_board_square("f8")),
                        Knight("black", chess_notation_to_board_square("g8")),
                        Rook("black", chess_notation_to_board_square("h8")),
                        Pawn("black", chess_notation_to_board_square("a7")),
                        Pawn("black", chess_notation_to_board_square("b7")),
                        Pawn("black", chess_notation_to_board_square("c7")),
                        Pawn("black", chess_notation_to_board_square("d7")),
                        Pawn("black", chess_notation_to_board_square("e7")),
                        Pawn("black", chess_notation_to_board_square("f7")),
                        Pawn("black", chess_notation_to_board_square("g7")),
                        Pawn("black", chess_notation_to_board_square("h7")),
        ]
    board.add_pieces(
        #test_setup
        standard_setup
        #rook_checkmate
        #queen_king_checkmate1
        #rook_endgame
        #in_check1
        #queenside_castling
    )

    #main game loop
    

    #print the board
    clear()
    board.update_all_pieces_influence()
    board.update_attack_and_protect_status()
    clear()
    #board.display_all_pieces_influence()
    board.display_all_square_attack_status()
    #board.display_all_pieces_protected()
    board.display()
    board.game_over = board.check_game_over()

    #TIP: Input is formated in typical chess notation
    #    Ex: a4, or Re5

    while not board.game_over:
        #get input
        print(">", end = '')
        player_in = input()

        clear()
        board.move(player_in)  #move the desired piece
        board.display_all_square_attack_status()
        board.display()
        board.game_over = board.check_game_over()
        
        if not board.game_over:
            if board.white_turn:
                print("White's turn to move.")
            else:
                print("Black's turn to move.")

    print("Bye bye. See you next time!")
    
        
        
    

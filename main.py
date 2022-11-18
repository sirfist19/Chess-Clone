#this is a text based Chess game in python
from pieces import *
from essential_fxns import *
from board import Board
from board_setups import *

if __name__ == "__main__":
    board = Board()
    
    board.add_pieces(
        #test_setup
        standard_setup
        #pinned_queen
    )

    clear()
    board.update_all_pieces_influence()
    board.update_attack_and_protect_status()
    clear()
    #board.display_all_pieces_influence()
    board.display_all_square_attack_status()
    #board.display_all_pieces_protected()
    board.display()
    board.game_over = board.check_game_over()

    #TIP: Input is formated in typical algebraic chess notation
    #    Ex: a4, or Re5

    #main game loop
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
    
        
        
    

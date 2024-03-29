#this is a text based Chess game in python
from pieces import *
from essential_fxns import *
from board import Board
from board_setups import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

if __name__ == "__main__":
    board = Board()
    
    board.add_pieces(
        #test_setup
        standard_setup
        #pinned_queen
        #bishop_influence_test
        #testing_checkmate
        #in_check1
        #pawn_promotion
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
    
    def draw_grid():
        for i in range(8):
            for j in range(8):
                rect = pygame.Rect(i*TILE_WIDTH , j*TILE_WIDTH, TILE_WIDTH, TILE_WIDTH)
                if i%2==0: # even row
                    if j%2==0:
                        pygame.draw.rect(screen, dark_color, rect)
                    else:
                        pygame.draw.rect(screen, light_color, rect)
                else:
                    if j%2==0:
                        pygame.draw.rect(screen, light_color, rect)
                    else:
                        pygame.draw.rect(screen, dark_color, rect)

    #main game loop
    while True:#not board.game_over:
        #get input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)
        draw_grid()
        board.draw_pieces(screen)
        pygame.display.update()

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
        
        
        clock.tick(FPS)
    print("Bye bye. See you next time!")
    
        
        
    

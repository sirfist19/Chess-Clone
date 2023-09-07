import os
import pygame, sys
from pygame.locals import *
pygame.init()

# colors 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
light_blue = (0, 0, 150)
green = (0, 255, 0)
light_gray = (178, 190, 181)
golden_brown = (153, 101, 21)
gray = (60, 60, 60)
gold = (0xff, 0xd7, 0x00)
brown = (0x96, 0x4B, 0x00) #964B00

dark_color = golden_brown
light_color = white

WIDTH = 800
HEIGHT = 800
NUM_TILES_WIDE = 8
NUM_TILES_TALL = 8
TILE_WIDTH = 100
FPS = 60

def chess_notation_to_board_square(player_square):
    x_char = player_square[0]
    y_char = int(player_square[1])

    x_mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    #1 -> 7
    #2 -> 6
    #8 -> 0
    x_coord = x_mapping[x_char]
    y_coord = 8 - y_char
    return [x_coord, y_coord]

def remove_invalid_squares(squares):
    res = []
    for square in squares:
        if square[0] >= 0 and square[0] < 8 and square[1] >= 0 and square[1] < 8:
            res.append(square)
    return res

def process_input(player_input): 
    #Example possible moves:
    #Ra2
    #e4
    #Kf3
    #xd6
    #Nxg7
    #O-O
    #O-O-O

    #want to get the piece to move (or that piece's square)
    #and the desired square
    #player_input = player_input.lower()
    kingside_castling = (player_input == "O-O" 
                    or player_input == "o-o" )
    queenside_castling = (player_input == "o-o-o" 
                    or player_input == "O-O-O")
    if kingside_castling:
        return "kingside castling"
    if queenside_castling:
        return "queenside castling"

    type_of_piece_to_move = identify_type_of_piece_to_move(player_input[0])
    des_square = chess_notation_to_board_square(player_input[-2:]) #the last two chars of player_input
    return [type_of_piece_to_move, des_square]
    

def identify_type_of_piece_to_move(first_letter):
    is_pawn = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    if first_letter in is_pawn:
        return "Pawn"
    elif first_letter == 'n' or first_letter == 'N':
        return "Knight"
    elif first_letter == 'B':
        return "Bishop"
    elif first_letter == 'k' or first_letter == 'K':
        return "King"
    elif first_letter == 'q' or first_letter == 'Q':
        return "Queen"
    elif first_letter == 'r' or first_letter == 'R':
        return "Rook"
    else:
        return "ERROR IN PIECE IDENTIFICATION"

def invalid_move(player_square):
    #if len(player_square) != 4:
    #    print("Invalid move. Please try again!")
    #    return True
    castling_input = (player_square == "O-O" 
                    or player_square == "o-o" 
                    or player_square == "o-o-o" 
                    or player_square == "O-O-O")
    if castling_input:
        return False #castling is a valid input

    x_char = player_square[-2]
    y_char = player_square[-1]
    if not y_char.isnumeric():
        return True

    y_char = int(y_char)
    valid_x = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    if x_char not in valid_x or y_char < 1 or y_char > 8:
        print("Invalid move. Please try again!")
        return True
    return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
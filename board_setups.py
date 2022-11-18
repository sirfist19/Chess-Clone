from pieces import *
from essential_fxns import *

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

pins = [
    King("white", chess_notation_to_board_square("d8")),
    King("black", chess_notation_to_board_square("b1")),
    Knight("white", chess_notation_to_board_square("d5")),
    Rook("black", chess_notation_to_board_square("d1"))
]
pinned_queen = [
    King("black", chess_notation_to_board_square("d8")),
    King("white", chess_notation_to_board_square("b1")),
    Queen("black", chess_notation_to_board_square("f6")),
    Bishop("white", chess_notation_to_board_square("h4")),
    Pawn("white", chess_notation_to_board_square("g3"))
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
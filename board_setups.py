from pieces import *
from essential_fxns import *

empty_board = []
test_setup = [
       King("white", "e4"),
       King("black", "a8"),
       Pawn("white", "e2"),
       Pawn("white", "f2"),
       Pawn("white", "g2"),
       Pawn("white", "h2"),
       Pawn("black", "e6"),
       Pawn("white", "d6"),
       Rook("white", "a1"),
       #Bishop("black", "e4"))
    ]
pawn_promotion = [
    King("white", "a1"),
    King("black", "f5"),
    Pawn("white", "f7")
]
rook_checkmate = [
                        Rook("white", "a8"),
                        Rook("white", "b7"),
                        King("black", "e8"),
                        King("white", "e1")
                ]
rook_checkmate2 = [
                        Rook("black", "a8"),
                        Rook("black", "b7"),
                        King("white", "e8"),
                        King("black", "e1")
                ]
queen_king_checkmate1 = [
                        Queen("black", "e7"),
                        King("black", "e6"),
                        King("white", "e8")
                ]
rook_endgame = [
                        Rook("white", "a8"),
                        King("white", "d3"),
                        King("black", "d5")

    ]
testing_checkmate = [
    King("white", "e8"),
    King("black", "e6"),
    Rook("black", "a8"),
    Rook("white", "c1")
]
bishop_influence_test = [
    King("black", "e8"),
    King("white", "e6"),
    Bishop("white", "c3"),
    Pawn("black", "e5")
]

pins = [
    King("white", "d8"),
    King("black", "b1"),
    Knight("white", "d5"),
    Rook("black", "d1")
]
pinned_queen = [
    King("black", "d8"),
    King("white", "b1"),
    Queen("black", "f6"),
    Bishop("white", "h4"),
    Pawn("white", "g3"),
    Pawn("black", "a6")
]

in_check1 = [
       King("white", "e1"),
       King("black", "a8"),
       Pawn("white", "e2"),
       Pawn("white", "f2"),
       Pawn("white", "g2"),
       Pawn("white", "h2"),
       #Pawn("white", "d2")),
       Pawn("black", "e6"),
       Pawn("black", "d6"),
       Rook("black", "a1"),
       Bishop("black", "e4")
    ]
kingside_castling = [
        King("white", "e1"),
        Rook("white", "h1"),
        King("black", "e8"),
        Rook("black", "h8")
    ]
queenside_castling = [
        King("white", "e1"),
        Rook("white", "a1"),
        King("black", "e8"),
        Rook("black", "a8")
    ]
standard_setup = [
                        #white
                        Rook("white", "a1"),
                        Knight("white", "b1"),
                        Bishop("white", "c1"),
                        Queen("white", "d1"),
                        King("white", "e1"),
                        Bishop("white", "f1"),
                        Knight("white", "g1"),
                        Rook("white", "h1"),
                        Pawn("white", "a2"),
                        Pawn("white", "b2"),
                        Pawn("white", "c2"),
                        Pawn("white", "d2"),
                        Pawn("white", "e2"),
                        Pawn("white", "f2"),
                        Pawn("white", "g2"),
                        Pawn("white", "h2"),
                                

                        #black
                        Rook("black", "a8"),
                        Knight("black", "b8"),
                        Bishop("black", "c8"),
                        Queen("black", "d8"),
                        King("black", "e8"),
                        Bishop("black", "f8"),
                        Knight("black", "g8"),
                        Rook("black", "h8"),
                        Pawn("black", "a7"),
                        Pawn("black", "b7"),
                        Pawn("black", "c7"),
                        Pawn("black", "d7"),
                        Pawn("black", "e7"),
                        Pawn("black", "f7"),
                        Pawn("black", "g7"),
                        Pawn("black", "h7"),
        ]
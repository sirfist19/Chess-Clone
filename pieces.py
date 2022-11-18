#all the chess pieces classes
from essential_fxns import *

class Pawn:  
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.value = self.get_value_given_color()
        self.name = "Pawn"
        self.influence = []
        self.has_moved = False
        self.protected = False

    def get_value_given_color(self):
        if self.color == "white":
            return 'P'
        if self.color == 'black':
            return 'p'
        return ''
    
    def piece_is_blocking(self, des_coord):
        return [] #it is not possible for a piece to be blocking

    def set_influence(self): #gives the squares that the pawn attacks
        if self.color == "white":
            temp = [
                    [self.coord[0] + 1, self.coord[1] - 1], #square above and right
                    [self.coord[0] - 1, self.coord[1] - 1]]#square above and left
            self.influence = remove_invalid_squares(temp)
        elif self.color == "black":
            temp =  [
                    [self.coord[0] + 1, self.coord[1] + 1], #square below and right
                    [self.coord[0] - 1, self.coord[1] + 1] #square below and left
                   ]
            self.influence = remove_invalid_squares(temp)

    def move(self, des_coord, is_capturing):
        #print(is_capturing)
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])
        x_dist = abs(self.coord[0] - des_coord[0])
        y_dist = (self.coord[1] - des_coord[1])
       
        #01 02 -> negative
        #08 07 -> positive

        if x_same and y_same:
            print("You are moving the pawn to the same square it is already on. Please try again.")
            return False
        if self.color == "white": #only positive y_dist allowed
            if is_capturing: #if capturing then can only move one square forward and one square to the left or right
                if (y_dist != 1 or x_dist != 1):
                    print("Invalid pawn capture")
                    return False
            elif x_dist != 0: #if there is a change in the x-coord otherwise then it is invalid
                print("Invalid pawn move")
                return False
            elif self.has_moved == False: #if the pawn hasn't yet moved then can move 1 or 2 squares
                if y_dist < 1 or y_dist > 2: #should be 1 or 2
                    print("Invalid pawn move")
                    return False
            else: #only can move 1 square
                if y_dist == 2:
                    print("You can only move a pawn 2 spaces on its first move.")
                    return False
                if y_dist != 1:
                    print("Invalid pawn move")
                    return False
        
        if self.color == "black": #only negative y_dist allowed
            if is_capturing:
                if (y_dist != -1 or x_dist != 1):
                    print("Invalid pawn capture")
                    return False
            elif x_dist != 0:
                print("Invalid pawn move")
                return False
            elif self.has_moved == False:
                if y_dist < -2 or y_dist > -1: #should be -1 or -2
                    print("Invalid pawn move")
                    return False
            else:
                if y_dist == -2:
                    print("You can only move a pawn 2 spaces on its first move.")
                    return False
                if y_dist != -1: #should be -1
                    print("Invalid pawn move")
                    return False

        #move the pawn to the given square by calling the board to do the move
        #if self.has_moved == False:
        #    self.has_moved = True
        return True

class Knight:  
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.value = self.get_value_given_color()
        self.name = "Knight"
        self.protected = False
        self.has_moved = False
        self.influence = []

    def get_value_given_color(self):
        if self.color == "white":
            return 'N'
        if self.color == 'black':
            return 'n'
        return ''

    def piece_is_blocking(self, des_coord):
        return [] #it is not possible for a piece to be blocking

    def set_influence(self): #gives the squares that the pawn attacks
        x = self.coord[0]
        y = self.coord[1]
        temp = [
                [x + 1, y - 2], #right 1 up 2
                [x + 2, y - 1], #right 2 up 1
                [x + 2, y + 1], #right 2 down 1
                [x + 1, y + 2], #right 1 down 2

                [x - 1, y - 2], #left 1 up 2
                [x - 2, y - 1], #left 2 up 1
                [x - 2, y + 1], #left 2 down 1
                [x - 1, y + 2]  #left 1 down 2
               ]
        self.influence = remove_invalid_squares(temp)
        

    def move(self, des_coord):
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])
        x_dist = abs(self.coord[0] - des_coord[0])
        y_dist = abs(self.coord[1] - des_coord[1])
        valid_knight_move = (
            ((x_dist == 1) and (y_dist == 2)) or 
            ((x_dist == 2) and (y_dist == 1)))

        if x_same and y_same:
            print("You are moving the knight to the same square it is already on. Please try again.")
            return False
        if not valid_knight_move:
            print("Invalid knight move")
            return False
        
        #move the knight to the given square by calling the board to do the move
        return True

class Bishop:  
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.name = "Bishop"
        self.value = self.get_value_given_color()
        self.protected = False
        self.has_moved = False
        self.influence = []

    def get_value_given_color(self):
        if self.color == "white":
            return 'B'
        if self.color == 'black':
            return 'b'
        return ''

    def piece_is_blocking(self, des_coord):
        #x_same = (self.coord[0] == des_coord[0])
        #y_same = (self.coord[1] == des_coord[1])
        x_dist = des_coord[0] - self.coord[0] #positive if moving right
        y_dist = self.coord[1] - des_coord[1] #positive if moving up
        going_up = (y_dist > 0)
        going_down = (y_dist < 0)
        going_left = (x_dist < 0)
        going_right = (x_dist > 0)
        iterations = abs(x_dist)

        squares_to_check = []
        if going_up and going_left:
            for i in range(1, iterations):
                x = self.coord[0] - i
                y = self.coord[1] - i
                squares_to_check.append([x,y])
        elif going_up and going_right:
            for i in range(1, iterations):
                x = self.coord[0] + i
                y = self.coord[1] - i
                squares_to_check.append([x,y])
        elif going_down and going_left:
            for i in range(1, iterations):
                x = self.coord[0] - i
                y = self.coord[1] + i
                squares_to_check.append([x,y])
        elif going_down and going_right:
            for i in range(1, iterations):
                x = self.coord[0] + i
                y = self.coord[1] + i
                squares_to_check.append([x,y])
        return squares_to_check

    def set_influence(self): #gives the squares that the pawn attacks
        x = self.coord[0]
        y = self.coord[1]
        pos_diag = [[x + i, y + i] for i in range(-7, 8) if i != 0]
        neg_diag = [[x - i, y + i] for i in range(-7, 8) if i != 0]
        temp = pos_diag + neg_diag
        self.influence = remove_invalid_squares(temp)

    def move(self, des_coord):
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])
        x_dist = abs(self.coord[0] - des_coord[0])
        y_dist = abs(self.coord[1] - des_coord[1])
        
        valid_bishop_move = (x_dist == y_dist)

        if x_same and y_same:
            print("You are moving the bishop to the same square it is already on. Please try again.")
            return False
        if not valid_bishop_move:
            print("Invalid bishop move")
            return False
        
        #move the rook to the given square by calling the board to do the move
        return True

class Rook:  
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.name = "Rook"
        self.value = self.get_value_given_color()
        self.protected = False
        self.has_moved = False
        self.influence = []

    def get_value_given_color(self):
        if self.color == "white":
            return 'R'
        if self.color == 'black':
            return 'r'
        return ''

    def piece_is_blocking(self, des_coord):
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])
        going_up = x_same and (self.coord[1] > des_coord[1])
        going_down = x_same and (self.coord[1] < des_coord[1])
        going_left = y_same and (self.coord[0] > des_coord[0])
        going_right = y_same and (self.coord[0] < des_coord[0])

        squares_to_check = []
        if going_up:
            squares_to_check = [[des_coord[0], i] for i in range(des_coord[1] + 1, self.coord[1])]
        elif going_down:
            squares_to_check = [[des_coord[0], i] for i in range(self.coord[1] + 1, des_coord[1])]
        elif going_left:
            squares_to_check = [[i, des_coord[1]] for i in range(des_coord[0] + 1, self.coord[0])]
        elif going_right:
            squares_to_check = [[i, des_coord[1]] for i in range(self.coord[0] + 1, des_coord[0])]
        return squares_to_check

    def set_influence(self): #gives the squares that the pawn attacks
        x = self.coord[0]
        y = self.coord[1]
        row = [[x + i, y] for i in range(-7, 8) if i != 0]
        file = [[x, y + i] for i in range(-7, 8) if i != 0]
        temp = row + file
        self.influence = remove_invalid_squares(temp)

    def move(self, des_coord):
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])

        if x_same and y_same:
            print("You are moving the rook to the same square it is already on. Please try again.")
            return False
        if not x_same and not y_same:
            print("Invalid rook move")
            return False
       
        #move the rook to the given square by calling the board to do the move
        return True

class Queen:  
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.name = "Queen"
        self.value = self.get_value_given_color()
        self.protected = False
        self.has_moved = False
        self.influence = []

    def get_value_given_color(self):
        if self.color == "white":
            return 'Q'
        if self.color == 'black':
            return 'q'
        return ''
    def piece_is_blocking(self, des_coord):
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])
        x_dist = des_coord[0] - self.coord[0] #positive if moving right
        y_dist = self.coord[1] - des_coord[1] #positive if moving up

        valid_bishop_move = (abs(x_dist) == abs(y_dist))
        valid_rook_move = (x_same or y_same)

        if valid_rook_move:
            going_up = x_same and (self.coord[1] > des_coord[1])
            going_down = x_same and (self.coord[1] < des_coord[1])
            going_left = y_same and (self.coord[0] > des_coord[0])
            going_right = y_same and (self.coord[0] < des_coord[0])

            squares_to_check = []
            if going_up:
                squares_to_check = [[des_coord[0], i] for i in range(des_coord[1] + 1, self.coord[1])]
            elif going_down:
                squares_to_check = [[des_coord[0], i] for i in range(self.coord[1] + 1, des_coord[1])]
            elif going_left:
                squares_to_check = [[i, des_coord[1]] for i in range(des_coord[0] + 1, self.coord[0])]
            elif going_right:
                squares_to_check = [[i, des_coord[1]] for i in range(self.coord[0] + 1, des_coord[0])]
            return squares_to_check
        elif valid_bishop_move:
            going_up = (y_dist > 0)
            going_down = (y_dist < 0)
            going_left = (x_dist < 0)
            going_right = (x_dist > 0)
            iterations = abs(x_dist)

            squares_to_check = []
            if going_up and going_left:
                for i in range(1, iterations):
                    x = self.coord[0] - i
                    y = self.coord[1] - i
                    squares_to_check.append([x,y])
            elif going_up and going_right:
                for i in range(1, iterations):
                    x = self.coord[0] + i
                    y = self.coord[1] - i
                    squares_to_check.append([x,y])
            elif going_down and going_left:
                for i in range(1, iterations):
                    x = self.coord[0] - i
                    y = self.coord[1] + i
                    squares_to_check.append([x,y])
            elif going_down and going_right:
                for i in range(1, iterations):
                    x = self.coord[0] + i
                    y = self.coord[1] + i
                    squares_to_check.append([x,y])
            return squares_to_check

    def set_influence(self): #gives the squares that the pawn attacks
        x = self.coord[0]
        y = self.coord[1]
        row = [[x + i, y] for i in range(-7, 8) if i != 0]
        file = [[x, y + i] for i in range(-7, 8) if i != 0]
        pos_diag = [[x + i, y + i] for i in range(-7, 8) if i != 0]
        neg_diag = [[x - i, y + i] for i in range(-7, 8) if i != 0]
        rook_temp = row + file
        bishop_temp = pos_diag + neg_diag
        temp = rook_temp + bishop_temp
        self.influence = remove_invalid_squares(temp)

    def move(self, des_coord):
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])
        x_dist = abs(self.coord[0] - des_coord[0])
        y_dist = abs(self.coord[1] - des_coord[1])
        
        valid_bishop_move = (x_dist == y_dist)
        valid_rook_move = (x_same or y_same)

        if x_same and y_same:
            print("You are moving the queen to the same square it is already on. Please try again.")
            return False
        if not valid_rook_move and not valid_bishop_move:
            print("Invalid queen move")
            return False
        
        #move the rook to the given square by calling the board to do the move
        return True

class King:  
    def __init__(self, color, coord):
        self.color = color
        self.coord = coord
        self.name = "King"
        self.value = self.get_value_given_color()
        self.protected = False
        self.has_moved = False
        self.influence = []

    def piece_is_blocking(self, des_coord):
        return [] #it is not possible for a piece to be blocking

    def get_value_given_color(self):
        if self.color == "white":
            return 'K'
        if self.color == 'black':
            return 'k'
        return ''

    def set_influence(self):
        x = self.coord[0]
        y = self.coord[1]
        temp = [[x + i, y + j] for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
        self.influence = remove_invalid_squares(temp)

    def move(self, des_coord):
        x_same = (self.coord[0] == des_coord[0])
        y_same = (self.coord[1] == des_coord[1])
        x_dist = abs(self.coord[0] - des_coord[0])
        y_dist = abs(self.coord[1] - des_coord[1])
        valid_king_move = ((x_dist < 2) and (y_dist < 2)) 

        if x_same and y_same:
            print("You are moving the king to the same square it is already on. Please try again.")
            return False
        if not valid_king_move:
            print("Invalid king move")
            return False
        
        #move the king to the given square by calling the board to do the move
        return True


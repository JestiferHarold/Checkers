from enums import PieceColors, BoardColor

class Piece:
    def __init__(self, color: PieceColors):
        self.color = color
        self.is_front_player = True

    def __instancecheck__(self, instance):
        return isinstance(instance, Piece)
    

class SuperPiece(Piece):
    pass

class NullCharacter:
    def __init__(self, color: PieceColors):
        self.color = color

class Board:
    def __init__(self):
        self.board = list()
        self.red_move = True
        for i in range(8):
            self.board.append(list())

    def move(self, instance: Piece):   
        if self.red_move and instance.color == PieceColors.RED:
            pass
    

class Player:
    def __init__(self, color: PieceColors):
        self.piece_color = color
        self.alive = 12
        self.dead = 0
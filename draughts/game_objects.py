from pygame import Surface, draw
from .enums_and_constants import BoardColor, ROWS, BLOCK_SIZE, COLS, PieceColors
from .piece import Piece

class Board:
    def __init__(self):
        self.board = list()
        self.selected_piece = None
        self.red_alive = self.white_alive = 12
        self.red_kings_alive = self.white_kings_alive = 0
        self.create_board()

    def draw_squares(self, surface: Surface):
        surface.fill((0, 0, 0))
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                draw.rect(surface, BoardColor.RED, (row * BLOCK_SIZE, col * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == PieceColors.WHITE:
                self.white_kings_alive += 1
            else:
                self.red_kings_alive += 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append(list())
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, PieceColors.WHITE))

                    elif row > 4:
                        self.board[row].append(Piece(row, col, PieceColors.RED))
                    
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, screen):
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)
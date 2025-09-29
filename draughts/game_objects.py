from pygame import Surface, draw
from .enums_and_constants import BoardColor, ROWS, BLOCK_SIZE, COLS, PieceColors
from .piece import Piece
from typing import List, Dict

class Board:
    def __init__(self) -> None:
        self.board = list()
        self.selected_piece: Piece | None = None
        self.red_alive: int = 12 
        self.white_alive: int = 12
        self.red_kings_alive: int = 0
        self.white_kings_alive:int = 0
        self.create_board()

    def draw_squares(self, surface: Surface) -> None:
        surface.fill((0, 0, 0))
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                draw.rect(surface, BoardColor.RED.value, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move(self, piece: Piece, row: int, col: int) -> None:
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == PieceColors.WHITE:
                self.white_kings_alive += 1
            else:
                self.red_kings_alive += 1

    def get_piece(self, row: int, col: int) -> Piece | int:
        return self.board[row][col]

    def create_board(self) -> None:
        for row in range(ROWS):
            self.board.append(list())
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        p = Piece(row, col, PieceColors.WHITE)
                        p.calculate_position()
                        self.board[row].append(p)

                    elif row > 4:
                        p = Piece(row, col, PieceColors.RED)
                        p.calculate_position()
                        self.board[row].append(p)
                    
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
        
    def draw(self, screen: Surface) -> None:
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def remove(self, pieces: List[Piece]) -> None:
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == PieceColors.RED:
                    self.red_alive -= 1
                else:
                    self.white_alive -= 1
        
    def winner(self) -> PieceColors | None:
        if self.red_alive <= 0:
            return PieceColors.WHITE
        elif self.white_alive <= 0:
            return PieceColors.RED
        else:
            return None
    
    def evaluate(self) -> int:
        return self.white_alive - self.red_alive + (self.white_kings_alive * 0.5 - self.red_kings_alive * 0.5)
    
    def get_all_pieces(self, color: PieceColors) -> List[Piece]:
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)

        return pieces

    def get_valid_moves(self, piece: Piece) -> Dict:
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == PieceColors.RED or piece.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == PieceColors.WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves

    def _traverse_left(self, start: int, stop: int, step: int, color: PieceColors, left: int, skipped: List = []) -> Dict:
        moves: Dict = {}
        last: List = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current: Piece | int = self.board[r][left]

            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row: int = max(r - 3, 0)
                    else:
                        row: int = min(r + r, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, left - 1, last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1, last))
                    break
            elif current.color == color:
                break

            else:
                last = [current]

            left -= 1
        return moves

    def _traverse_right(self, start: int, stop: int, step: int, color: PieceColors, right: int, skipped: List = []) -> Dict:
        moves: Dict = {}
        last: List = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current: Piece | int = self.board[r][right]

            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row: int = max(r - 3, 0)
                    else:
                        row: int = min(r + r, ROWS)

                    moves.update(self._traverse_left(r + step, row, step, color, right - 1, last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1, last))
                    break
            elif current.color == color:
                break

            else:
                last = [current]

            right += 1

        return moves
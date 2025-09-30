import pygame
from .game_objects import Board
from .enums_and_constants import PieceColors, BLOCK_SIZE
from .piece import Piece
from typing import Dict

class Game:
  def __init__(self, screen: pygame.Surface):
    self.selected: Piece | None = None
    self.board: Board = Board()
    self.turn: PieceColors = PieceColors.RED
    self.valid_moves: Dict = dict()
    self.screen: pygame.Surface = screen

  def update(self) -> None:
    self.board.draw(self.screen)
    self.draw_valid_moves(self.valid_moves)
    pygame.display.update()

  def _game_start(self) -> None:
    self.selected = None
    self.board = Board()
    self.turn = PieceColors.RED
    self.valid_moves = dict()

  def reset(self) -> None:
    self._game_start()

  def select(self, row: int, col: int) -> bool:
    if self.selected:
      result = self._move(row, col)
      if not result:
        self.selected = None
        return self.select(row, col)

    piece = self.board.get_piece(row, col)

    if piece != 0 and piece.color == self.turn:
      self.selected = piece
      self.valid_moves = self.board.get_valid_moves(piece)
      return True
  
    return False

  def _move(self, row: int, col: int) -> bool:    
    piece = self.board.get_piece(row, col)
    if self.selected and piece == 0 and (row, col) in self.valid_moves:
      self.board.move(self.selected, row, col)
      skipped = self.valid_moves[(row, col)]
      if skipped:
        self.board.remove(skipped)
      self.change_turn()      
    else:
      
      return False
  
    return True
  
  def winner(self) -> PieceColors | None:
    return self.board.winner()
  
  #complete this
  def draw_valid_moves(self, moves) -> None:
    for move in moves:
      row, col = move
      pygame.draw.circle(self.screen, PieceColors.BLUE.value, (col * BLOCK_SIZE + BLOCK_SIZE // 2, row * BLOCK_SIZE + BLOCK_SIZE // 2), 15)

  def change_turn(self) -> None:
    self.valid_moves = dict()
    if self.turn == PieceColors.RED:
      self.turn = PieceColors.WHITE
    else:
      self.turn = PieceColors.RED

  def get_board(self) -> Board:
    return self.board
  
  def ai_move(self, board: Board):
    if board != None:
      self.board = board
      
    self.change_turn()
    self.selected = None
    self.valid_moves = {}
import pygame
from .game_objects import Board
from .enums_and_constants import PieceColors, BLOCK_SIZE

class Game:
  def __init__(self, screen: pygame.Surface) -> None:
    self._game_start()
    self.screen = screen

  def update(self):
    self.board.draw(self.screen)
    self.draw_valid_moves(self.valid_moves)
    pygame.display.update()

  def _game_start(self):
    self.selected = None
    self.board = Board()
    self.turn = PieceColors.RED
    self.valid_moves = dict()

  def reset(self):
    self._game_start()

  def select(self, row, col):
    if self.selected:
      result = self.move(row, col)
      if not result:
        self.selected = None
        self.select(row, col)

    piece = self.board.get_piece(row, col)

    if piece != 0 and piece.color == self.turn:
      self.selected = piece
      self.valid_moves = self.board.get_valid_moves(piece)
      return True
  
    return False

  def _move(self, row, col):    
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
  
  def winner(self):
    return self.board.winner()
  
  def draw_valid_moves(self, moves):
    for move in moves:
      row, col = move
      pygame.draw.circle(self.screen, PieceColors.BLUE, (col * BLOCK_SIZE + BLOCK_SIZE // 2, row * BLOCK_SIZE + BLOCK_SIZE // 2), 50)

  def change_turn(self):
    self.valid_moves = dict()
    if self.turn == PieceColors.RED:
      self.turn = PieceColors.WHITE
    else:
      self.turn = PieceColors.RED
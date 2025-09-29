import pygame
from .enums_and_constants import PieceColors, BLOCK_SIZE, KINGS_CROWN

class Piece:

  PADDING = 10
  BORDER = 2

  def __init__(self, row, col, color):
    self.row = row
    self.col = col
    self.color = color
    self.king = False
    if self.color == PieceColors.WHITE:
      self.direction = -1
    else:
      self.direction = 1

    self.x = self.y = 0

  def calculate_position(self):
    self.x = BLOCK_SIZE * self.col + BLOCK_SIZE // 2
    self.y = BLOCK_SIZE * self.row + BLOCK_SIZE // 2

  def make_king(self):
    self.king = True

  def draw(self, screen):
    radius = BLOCK_SIZE // 2 - Piece.PADDING
    pygame.draw.circle(screen, self.color, (self.x, self.y), radius + Piece.BORDER)
    pygame.draw.circle(screen, PieceColors.GREY, (self.x, self.y), radius)
    if self.king:
      screen.blit(KINGS_CROWN, (self.x - KINGS_CROWN.get_width() // 2, self.y - KINGS_CROWN.get_height() // 2))

  def move(self, row, col):
    self.row = row
    self.col = col
    self.calculate_position()

  def __repr__(self):
    return str(self.color)
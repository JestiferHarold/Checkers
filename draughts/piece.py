import pygame
from .enums_and_constants import PieceColors, BLOCK_SIZE, KINGS_CROWN

class Piece:

  PADDING: int = 10
  BORDER: int = 2

  def __init__(self, row: int, col: int, color: PieceColors) -> None:
    self.row: int = row
    self.col: int = col
    self.color: PieceColors = color
    self.king: bool = False
    self.x: int = 0
    self.y: int = 0

  def calculate_position(self) -> None:
    self.x = BLOCK_SIZE * self.col + BLOCK_SIZE // 2
    self.y = BLOCK_SIZE * self.row + BLOCK_SIZE // 2

  def make_king(self) -> None:
    self.king = True

  def draw(self, screen: pygame.Surface) -> None:
    radius: float = BLOCK_SIZE // 2 - Piece.PADDING
    pygame.draw.circle(screen, self.color.value, (self.x, self.y), radius + Piece.BORDER)
    pygame.draw.circle(screen, PieceColors.GREY.value, (self.x, self.y), radius)
    if self.king:
      screen.blit(KINGS_CROWN, (self.x - KINGS_CROWN.get_width() // 2, self.y - KINGS_CROWN.get_height() // 2))

  def move(self, row: int, col: int) -> None:
    self.row = row
    self.col = col
    self.calculate_position()

  def __repr__(self) -> str:
    return str(self.color)
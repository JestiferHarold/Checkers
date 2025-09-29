import pygame
from draughts import HEIGHT, WIDTH, Board, BLOCK_SIZE, Game, PieceColors
from algorithms import minimax
from typing import Tuple

running: bool = True
FPS: int = 120
screen: pygame.Surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Draughts")
clock: pygame.time.Clock = pygame.time.Clock()
game: Game = Game(screen)

def get_row_and_col_from_mouse(position: Tuple[int, int]) -> Tuple[int, int]:
  x, y =  position
  row = y // BLOCK_SIZE
  col = x // BLOCK_SIZE

  return row, col

while running:
  clock.tick(FPS)

  if game.turn == PieceColors.WHITE:
    value, new_board = minimax(game.get_board(), 3, PieceColors.WHITE, game)
    game.ai_move(new_board)

  if game.turn == PieceColors.RED:
    value, new_board = minimax(game.get_board(), 3, PieceColors.RED, game)
    game.ai_move(new_board)

  if game.winner() != None:
    print(game.winner())
    break

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      row, col = get_row_and_col_from_mouse(pygame.mouse.get_pos())
      if game.turn == PieceColors.RED:
        game.select(row, col)

  game.update()


pygame.quit() 
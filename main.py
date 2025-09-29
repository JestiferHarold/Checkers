import pygame
from draughts import HEIGHT, WIDTH, Board, BLOCK_SIZE, Game, PieceColors

running: bool = True
FPS: int = 120
screen: pygame.Surface = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Draughts")
clock: pygame.time.Clock = pygame.time.Clock()
game: Game = Game(screen)

def get_row_and_col_from_mouse(position):
  x, y =  position
  row = y // BLOCK_SIZE
  col = x // BLOCK_SIZE

  return row, col

while running:
  clock.tick(FPS)

  game.

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      row, col = get_row_and_col_from_mouse(pygame.mouse.get_pos())
      if game.turn == PieceColors.RED:
        game.select(row, col)

  game.update()


pygame.quit() 
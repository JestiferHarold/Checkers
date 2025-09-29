import pygame
from draughts import HEIGHT, WIDTH, Board, BLOCK_SIZE

running: bool = True
FPS: int = 120
board: Board = Board()
screen: pygame.Surface = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Draughts")
clock: pygame.time.Clock = pygame.time.Clock()
piece = board.get_piece(0, 1)
board.move(piece, 4, 3)

def get_row_and_col_from_mouse(position):
  x, y =  position
  row = y // BLOCK_SIZE
  col = x // BLOCK_SIZE

  return row, col

while running:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      row, col = get_row_and_col_from_mouse(pygame.mouse.get_pos())
      piece = board.get_piece(row, col)
      board.move(piece, 4, 3)
    
  board.draw_squares(screen)
  pygame.display.update()


pygame.quit() 
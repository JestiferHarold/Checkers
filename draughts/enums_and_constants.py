from enum import Enum
import pygame

class PieceColors(Enum):
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACKss = (0, 0, 0)
    BLUE  = (0, 0, 255)
    GREY = (128, 128, 128)

class BoardColor(Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLS = 8
BLOCK_SIZE = WIDTH // COLS

image: pygame.Surface = pygame.image.load("draughts/assets/crown.png")
KINGS_CROWN = pygame.transform.scale(image,(45, 25))
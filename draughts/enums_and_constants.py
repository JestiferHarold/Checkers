from enum import Enum
from typing import Tuple
import pygame

class PieceColors(Enum):
    RED: Tuple[int, int, int] = (255, 0, 0)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    BLUE: Tuple[int, int, int]  = (0, 0, 255)
    GREY: Tuple[int, int, int] = (128, 128, 128)
    GREEN: Tuple[int, int, int] = (0, 255, 0)

class BoardColor(Enum):
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)

WIDTH: int = 800
HEIGHT: int = 800
ROWS: int = 8
COLS: int = 8
BLOCK_SIZE: int = WIDTH // COLS

image: pygame.Surface = pygame.image.load("draughts/assets/crown.png")
KINGS_CROWN: pygame.Surface = pygame.transform.scale(image,(45, 25))
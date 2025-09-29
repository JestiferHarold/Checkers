from enum import Enum
from typing import Tuple

class PieceColor(Enum):
  RED: Tuple[int, int, int] = (255, 0, 0)
  WHITE: Tuple[int, int, int] = (0, 0, 0)
  GREEN: Tuple[int, int, int] = (0, 255, 0)

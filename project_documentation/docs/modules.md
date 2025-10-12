# Modules

The project consists of two modules namely 

1. <a href = "#draughts">Draughts</a> and
2. <a href = "#algorithms">Algorithms</a>

Each of these modules play a significant role in the project.

---
<h3 id = "draughts">Draughts</h3>
---

The draughts module is a complete implementation of the draughts (checkers) game built with Pygame. It provides a modular architecture separating concerns into board management, game logic, piece representation, and constants/enumerations. The module supports both human vs human and human vs AI gameplay with visual feedback for valid moves.

The <a href = "https://github.com/JestiferHarold/Draughts/tree/main/draughts" target = "_blank">draughts</a> module has the following 5 files

1. <a href = "https://github.com/JestiferHarold/Draughts/blob/main/draughts/__init__.py" target = "_blank">__init__.py</a>
2. <a href = "https://github.com/JestiferHarold/Draughts/blob/main/draughts/board.py" target = "_blank">board.py</a>
3. <a href = "https://github.com/JestiferHarold/Draughts/blob/main/draughts/enums_and_constants.py" target = "_blank">enums_and_constants.py</a>
4. <a href = "https://github.com/JestiferHarold/Draughts/blob/main/draughts/game.py" target = "_blank">game.py</a>
5. <a href = "https://github.com/JestiferHarold/Draughts/blob/main/draughts/piece.py" target = "_blank">piece.py</a>

```
The __init__.py file makes the directory into a package i.e. Draughts module.
```

```
The board.py file contains the Board class which manages the board game state, piece positions, move validation, and game evaluation.
```

```
The enums_and_constants.py file defines all the game constants, enumerations and other resources used in the game.
```

```
The game.py file contains the Game class which orchestrates the gameplay, manages turns, handle user interactions, and coordinate between board and pieces.
```

```
The piece.py file contains the Piece class that represents the individual pieces with their property and rendering logic.
```
---
<h3 id = "algorithms">Algorithms</h3>
---

This module provides the artificial intelligence engine for a draughts game, centered around the minimax algorithm for strategic move selection. It enables the computer opponent to think ahead multiple moves by simulating all possible game continuations and choosing the optimal path based on board evaluation scores. The file includes utilities for move simulation, optional visualization of the AI's thought process, and comprehensive move generation that considers all pieces and their valid moves while properly handling captures.

The <a href target = "_blank">algorithms</a> has <a href = "" target = "_blank">minimax.py</a> and <a href = "" target = "_blank">__init__.py</a> file.

```
The __init__.py file makes the directory into a package i.e. Draughts module.
```

```
The minimax.py file implements the AI logic for the draughts game using the minimax algorithm.
```
---
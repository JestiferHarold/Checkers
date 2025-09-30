from copy import deepcopy
from algorithms.enum import PieceColor
import pygame

def simulate_move(piece, move, board, game, skip):
  board.move(piece, move[0], move[1])

  if skip:
    board.remove(skip)

  return board

def draw_moves(game, board, piece):
  valid_moves = board.get_all_valid_moves(piece)
  board.draw(game.screen)
  pygame.draw.circle(game.screen, PieceColor.GREEN.value, (piece.x, piece.y), 50, 5)
  game.draw_valid_moves(valid_moves.keys())
  pygame.display.update()
  pygame.time.delay(100)

def get_all_moves(board, color, game):
  moves = []

  for piece in board.get_all_pieces(color):
    valid_moves = board.get_valid_moves(piece)
    for move, skip in valid_moves.items():
      draw_moves(game, board, piece)
      temp_board = deepcopy(board)
      temp_piece = temp_board.get_piece(piece.row, piece.col)
      new_board = simulate_move(temp_piece, move, temp_board, game, skip)
      moves.append(new_board)
  
  return moves

def minimax(position, depth, max_player, game):
  if depth == 0 or position.winner() is not None:
    return position.evaluate(), position
  
  if max_player:
    max_eval = float("-inf")
    best_move = None
    
    for move in get_all_moves(position, PieceColor.WHITE, game):
      evaluation = minimax(move, depth - 1, False, game)[0]
      max_eval = max(max_eval, evaluation)
      if max_eval == evaluation:
        best_move = move
    return max_eval, best_move
  
  else:
    min_eval = float("inf")
    best_move = None
    
    for move in get_all_moves(position, PieceColor.RED, game):
      evaluation = minimax(move, depth - 1, True, game)[0]
      min_eval = min(min_eval, evaluation)
    
      if min_eval == evaluation:
        best_move = move
    return min_eval, best_move
  
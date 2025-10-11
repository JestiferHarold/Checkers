from copy import deepcopy
from draughts.enums_and_constants import PieceColors
import pygame

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.screen)
    pygame.draw.circle(game.screen, PieceColors.GREEN.value, (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(100)

def get_all_moves(board, color, game, visualize=False):
    moves = []
    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            if visualize:  # Only draw if explicitly requested
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
        moves = get_all_moves(position, PieceColors.WHITE, game, visualize=False)
        
        if not moves:
            return position.evaluate(), position
        
        for move in moves:
            evaluation, _ = minimax(move, depth - 1, False, game)
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
        
        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        moves = get_all_moves(position, PieceColors.RED, game, visualize=False)
        
        if not moves:
            return position.evaluate(), position
        
        for move in moves:
            evaluation, _ = minimax(move, depth - 1, True, game)
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
        
        return min_eval, best_move
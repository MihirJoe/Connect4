import numpy as np
import math
import random
from board import *

# Create non-minimax methods for AI decision making? 
    # Compare these methods to minimax with alpha-beta.

def minimax_alphabeta(board, moveCount, depth, alpha, beta, maximizingPlayer):
    valid_columns = all_valid_columns(board)
    random.shuffle(valid_columns)

    # Setup to leave recursion if at depth limit or if the board contains a win.
    if depth == 0:
        return None, score_board(board, AI)
    if is_end_node(board):
        if is_win(board, AI):
            return None, 9999999 - moveCount
        if is_win(board, PLAYER):
            return None, -9999999 + moveCount
        else:
            return None, 0
    
    # Maximizing player section.
        # Will start by setting "value = -math.inf", the initial best possible value achievable for the maximizer.
        # Should loop through all open/valid columns because these are the possible moves for the player.
        # Recursion will be "new_score = minimax(temp_board, depth - 1, alpha, beta, False)".
        # If this new score is greater than value, then update value to the new score and set the column to be returned.
        # Will include "alpha = max(alpha, value)" where value is the value/utilitiy of the board/node.
    if maximizingPlayer:
        bestScore = -math.inf
        for col in valid_columns:
            boardCopy = board.copy()
            add_token(boardCopy, col, AI)
            newScore = minimax_alphabeta(boardCopy, moveCount + 1, depth - 1, alpha, beta, False)[1]
            if newScore > bestScore:
                bestScore = newScore
                column = col
            alpha = max(alpha, bestScore)
            if alpha >= beta:
                break
        return column, bestScore

    # Minimizing player section.
        # Will start by setting "value = math.inf", the initial best possible value achievable for the minimizer.
        # Should loop through all open/valid columns.
        # Recursion will be the same as maximizing section.
        # If this new score is less than value, then update value to the new score and set the column to be returned.
        # Will include "beta = min(beta, value)".
    else:
        bestScore = math.inf
        for col in valid_columns:
            boardCopy = board.copy()
            add_token(boardCopy, col, PLAYER)
            newScore = minimax_alphabeta(boardCopy, moveCount + 1, depth - 1, alpha, beta, True)[1]
            if newScore < bestScore:
                bestScore = newScore
                column = col
            beta = min(beta, bestScore)
            if alpha >= beta:
                break
        return column, bestScore

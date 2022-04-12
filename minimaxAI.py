import numpy as np
import math
import random
from board import *
import settings

# implements minimax with alpha beta pruning
def minimax_alphabeta(board, moveCount, depth, alpha, beta, maximizingPlayer):
    valid_columns = all_valid_columns(board)
    random.shuffle(valid_columns) # shuffle the valid columns so do not always search in the same order

    # Setup to leave recursion if at depth limit or if the board contains a win.
    # if the depth is reached, return current value of the heuristic
    if depth == 0:
        return None, score_board(board, settings.AI)
    # if the board is full or has a win with the theoretical move
    if is_end_node(board):
        # return score of win for AI while factoring in number of moves
        if is_win(board, settings.AI):
            return None, 9999999 - moveCount
        # return score of win for player while factoring in number of moves
        if is_win(board, settings.PLAYER):
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
        bestScore = -math.inf # initialize best score
        for col in valid_columns:
            boardCopy = board.copy()
            add_token(boardCopy, col, settings.AI)
            newScore = minimax_alphabeta(boardCopy, moveCount + 1, depth - 1, alpha, beta, False)[1] # compute new score of theoretical move
            # update bestScore if newScore is better
            if newScore > bestScore:
                bestScore = newScore
                column = col
            # update alpha
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
        bestScore = math.inf # initialize best score
        for col in valid_columns:
            boardCopy = board.copy()
            add_token(boardCopy, col, settings.PLAYER)
            newScore = minimax_alphabeta(boardCopy, moveCount + 1, depth - 1, alpha, beta, True)[1]
            # if newScore is less than bestScore (better option), update best score
            if newScore < bestScore:
                bestScore = newScore
                column = col
            # update beta
            beta = min(beta, bestScore)
            if alpha >= beta:
                break
        return column, bestScore

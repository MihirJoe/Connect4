import numpy as np
import math
import random
from board import *

# Create non-minimax methods for AI decision making? 
    # Compare these methods to minimax with alpha-beta.

# NEED TO TEST THIS ON SIMPLER THINGS!! I THINK I NEED TO UPDATE THE  SCORE FUNCTION.
def minimax_alphabeta(board, depth, alpha, beta, maximizingPlayer):
    # Setup to leave recursion if at depth limit or if the board contains a win.
    valid_columns = all_valid_columns(board)
    if depth == 0:
        print("End of depth.")
        return None, score_board(board, AI)
    if is_end_node(board):
        if is_win(board, AI):
            print("AI Will Win.")
            return None, 9999999
        if is_win(board, PLAYER):
            print("Player Will Win.")
            return None, -9999999
        else:
            print("No one wins.")
            return None, 0
    
    # Maximizing player section.
        # Will start by setting "value = -math.inf", the initial best possible value achievable for the maximizer.
        # Should loop through all open/valid columns because these are the possible moves for the player.
        # Recursion will be "new_score = minimax(temp_board, depth - 1, alpha, beta, False)".
        # If this new score is greater than value, then update value to the new score and set the column to be returned.
        # Will include "alpha = max(alpha, value)" where value is the value/utilitiy of the board/node.
    if maximizingPlayer:
        bestScore = -math.inf
        #column = random.choice(valid_columns)
        for col in valid_columns:
            boardCopy = board.copy()
            add_token(boardCopy, col, AI)
            newScore = minimax_alphabeta(boardCopy, depth - 1, alpha, beta, False)[1]
            print("New Score Maximizer: ", newScore)
            if newScore > bestScore:
                bestScore = newScore
                column = col
            alpha = max(alpha, bestScore)
            if alpha >= beta:
                break
        print("Column Choice Maximizer: ", column)
        return column, bestScore

    # Minimizing player section.
        # Will start by setting "value = math.inf", the initial best possible value achievable for the minimizer.
        # Should loop through all open/valid columns.
        # Recursion will be the same as maximizing section.
        # If this new score is less than value, then update value to the new score and set the column to be returned.
        # Will include "beta = min(beta, value)".
    else:
        bestScore = math.inf
        #column = random.choice(valid_columns)
        for col in valid_columns:
            boardCopy = board.copy()
            add_token(boardCopy, col, PLAYER)
            newScore = minimax_alphabeta(boardCopy, depth - 1, alpha, beta, True)[1]
            print("New Score Minimizer: ", newScore)
            if newScore < bestScore:
                bestScore = newScore
                column = col
            beta = min(beta, bestScore)
            if alpha >= beta:
                break
        print("Column Choice Minimizer: ", column)
        return column, bestScore


board = create_board_df()
add_token(board,0,PLAYER)
add_token(board,0,PLAYER)
add_token(board,0,AI)
add_token(board,1,AI)
add_token(board,1,PLAYER)
add_token(board,2,PLAYER)
add_token(board,2,AI)
add_token(board,3,PLAYER)
add_token(board,3,PLAYER)
add_token(board,3,AI)
add_token(board,4,AI)
add_token(board,4,PLAYER)
add_token(board,4,AI)
add_token(board,5,AI)
add_token(board,5,PLAYER)
add_token(board,5,PLAYER)
add_token(board,5,PLAYER)
add_token(board,5,AI)


print(board)

colSelection, score = minimax_alphabeta(board, 1, -math.inf, math.inf, True)
print(type(colSelection))

if is_valid_column(board, colSelection):
    add_token(board, colSelection, AI)

print(board)
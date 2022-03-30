import numpy as np

def minimax_alphabeta(board, depth, alpha, beta, maximizing_player):
    # Setup to leave recursion if at depth limit or if the board contains a win.
    
    # Maximizing player section.
        # Will start by setting "value = -math.inf", the initial best possible value achievable for the maximizer.
        # Should loop through all open/valid columns because these are the possible moves for the player.
        # Recursion will be "new_score = minimax(temp_board, depth - 1, alpha, beta, False)".
        # If this new score is greater than value, then update value to the new score and set the column to be returned.
        # Will include "alpha = max(alpha, value)" where value is the value/utilitiy of the board/node.

    # Minimizing player section.
        # Will start by setting "value = math.inf", the initial best possible value achievable for the minimizer.
        # Should loop through all open/valid columns.
        # Recursion will be the same as maximizing section.
        # If this new score is less than value, then update value to the new score and set the column to be returned.
        # Will include "beta = min(beta, value)".

    # Return column selected and value.
        # Will need to have "minimax(...)[1]" for setting score in recursion, if using numpy matrix.

    pass
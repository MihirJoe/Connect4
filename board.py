import numpy as np
import pandas as pd
import time

ROWS = 6
COLS = 7
WIN_LENGTH = 4

TOP_ROW = 0

EMPTY = 0
PLAYER = 1
AI = 2

# Creates board as numpy matrix.
def create_board_matrix():
    board = np.zeros(ROWS, COLS)

# Create board as bitmap??
def create_board_bitmap():
    pass

# Create board as pandas dataframe.
def create_board_df():
    board = pd.DataFrame(EMPTY, index = range(ROWS), columns = range(COLS))
    return board

# Function to add a token to the board.
    # Will need to make sure it drops all the way to the lowest open row.
    # Assume the column is valid. We will make the if/else statement in the main loop.
def add_token(board, column, token):
    for row in range(ROWS):
        if board.iat[row, column] == EMPTY:
            lowest_row = row
    board.at[lowest_row, column] = token

# Function to check whether a column is open.
def is_valid_column(board, column):
    return board.iat[TOP_ROW, column] == EMPTY

# Function that returns all valid/open columns for a given board.
def all_valid_columns(board):
    valid_columns = []

    for col in range(COLS):
        if is_valid_column(board, col):
            valid_columns.append(col)

    return valid_columns

# Function to print the board, depending on choice for setup.
def print_board(board):
    pass

# Check if current board has a win (WIN_LENGTH consecutive tokens) for a given token.
def is_win(board, token):
    # Check horizontal directions.
    for row in range(ROWS):
        for col in range(COLS - (WIN_LENGTH - 1)):
            if all(board.iat[row, col+i] == token for i in range(WIN_LENGTH)):
                return True

    # Check vertical directions.
    for row in range(ROWS - (WIN_LENGTH - 1)):
        for col in range(COLS):
            if all(board.iat[row+i, col] == token for i in range(WIN_LENGTH)):
                return True

    # Check positive slopes.
    for row in range((WIN_LENGTH - 1), ROWS):
        for col in range(COLS - (WIN_LENGTH - 1)):
            if all(board.iat[row-i,col+i] == token for i in range(WIN_LENGTH)):
                return True


    # Check negative slopes.
    for row in range(ROWS - (WIN_LENGTH - 1)):
        for col in range(COLS - (WIN_LENGTH - 1)):
            if all(board.iat[row+i, col+i] == token for i in range(WIN_LENGTH)):
                return True

    return False

# Given a line (which will be of length WIN_LENGTH) and a token to check.
    # Will return the calculated score for the PLAYER/AI for that line.
    # Not sure how well it will work as the size of WIN_LENGTH increases.
    # Assuming WIN_LENGTH >= 4.
def score_line(line, token):
    score = 0
    oppToken = PLAYER
    if token == PLAYER: oppToken = AI

    if line.count(token) == WIN_LENGTH:
        return 9999999
    if line.count(oppToken) == WIN_LENGTH:
        return -9999999
    
    # Line scoring method for multiple WIN_LENGTH possibilities.
    for i in range(1, WIN_LENGTH):
        if line.count(token) == i and line.count(EMPTY) == (WIN_LENGTH - i):
            score += 2*i*i
        if line.count(oppToken) == i and line.count(EMPTY) == (WIN_LENGTH - i):
            score -= 2*i*i

    # Extra points for having tokens in center column?
    # Primary has WIN_LENGTH tokens: 1000
    # if line.count(token) == WIN_LENGTH:
    #     score += 1000
    
    # # Primary has 1 less than WIN_LENGTH tokens and 1 open space: 20
    # elif line.count(token) == (WIN_LENGTH - 1) and line.count(EMPTY) == 1:
    #     score += 20

    # # Primary has 2 less than WIN_LENGTH tokens and 2 open spaces: 5
    # elif line.count(token) == (WIN_LENGTH - 2) and line.count(EMPTY) == 2:
    #     score += 5

    # # Opponent has WIN_LENGTH tokens: -1000
    # if line.count(oppToken) == WIN_LENGTH:
    #     score -= 1000

    # # Opponent has 1 less than WIN_LENGTH tokens and 1 open space: -20
    # elif line.count(oppToken) == (WIN_LENGTH - 1) and line.count(EMPTY) == 1:
    #     score -= 20

    # # Opponent has 2 less than WIN_LENGTH tokens and 2 open spaces: -5
    # elif line.count(oppToken) == (WIN_LENGTH - 2) and line.count(EMPTY) == 2:
    #     score -= 5

    return score

# Function to return the score of a board for a player.
    # This will be the heuristic we use to determine the value of node/board.
def score_board(board, token):
    score = 0

    # Score horizontals.
    for row in range(ROWS):
        rowLine = list(board.iloc[row, :])
        for col in range(COLS - (WIN_LENGTH - 1)):
            lineSection = rowLine[col: col + WIN_LENGTH]
            score += score_line(lineSection, token)

    # Score verticals.
    for col in range(COLS):
        colLine = list(board.iloc[:, col])
        for row in range(ROWS - (WIN_LENGTH - 1)):
            lineSection = colLine[row: row + WIN_LENGTH]
            score += score_line(lineSection, token)

    # Score positive diagonals.
    for row in range(ROWS - (WIN_LENGTH - 1)):
        for col in range(COLS - (WIN_LENGTH - 1)):
            lineSection = list(board.iloc[row+i, col+i] for i in range(WIN_LENGTH))
            score += score_line(lineSection, token)

    # Score negative diagonals.
    for row in range(ROWS - (WIN_LENGTH - 1)):
        for col in range(COLS - (WIN_LENGTH - 1)):
            lineSection = list(board.iloc[row+(WIN_LENGTH - 1)-i, col+i] for i in range(WIN_LENGTH))
            score += score_line(lineSection, token)

    return score

# Function to check whether a board has a win or is full.
def is_end_node(board):
    return is_win(board, AI) or is_win(board, PLAYER) or (len(all_valid_columns(board)) == 0)




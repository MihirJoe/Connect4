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

# Function to check if current board has a win (four in a row) for a player.
def is_win(board, token):
    pass

# Function to return the score of a board for a player.
    # This will be the heuristic we use to determine the value of node/board.
def score_board(board, token):
    pass

# Function to check whether a board has a win or is full.
def is_end_node(board):
    pass

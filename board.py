import numpy as np
import pandas as pd
import settings

TOP_ROW = 0 # initialize TOP_ROW to 0, will remain constant

# Create board as pandas dataframe.
def create_board_df():
    board = pd.DataFrame(settings.EMPTY, index = range(settings.ROWS), columns = range(settings.COLS))
    return board

# Function to add a token to the board.
def add_token(board, column, token):
    for row in range(settings.ROWS):
        if board.iat[row, column] == settings.EMPTY:
            lowest_row = row
    board.at[lowest_row, column] = token # insert token at the lowest open row in column

# Function to check whether a column is open.
    # open as long as at least an empty spot in the top row.
def is_valid_column(board, column):
    return board.iat[TOP_ROW, column] == settings.EMPTY 

# Function that returns all valid/open columns for a given board.
def all_valid_columns(board):
    valid_columns = []
    # loop through columns and check validity
    for col in range(settings.COLS):
        if is_valid_column(board, col):
            valid_columns.append(col)

    return valid_columns

# Check if current board has a win (WIN_LENGTH consecutive tokens) for a given token.
def is_win(board, token):
    # Check horizontal directions.
    for row in range(settings.ROWS):
        for col in range(settings.COLS - (settings.WIN_LENGTH - 1)):
            if all(board.iat[row, col+i] == token for i in range(settings.WIN_LENGTH)):
                print("row win")
                return True

    # Check vertical directions.
    for row in range(settings.ROWS - (settings.WIN_LENGTH - 1)):
        for col in range(settings.COLS):
            if all(board.iat[row+i, col] == token for i in range(settings.WIN_LENGTH)):
                print("col win")
                return True

    # Check positive slopes.
    for row in range((settings.WIN_LENGTH - 1), settings.ROWS):
        for col in range(settings.COLS - (settings.WIN_LENGTH - 1)):
            if all(board.iat[row-i,col+i] == token for i in range(settings.WIN_LENGTH)):
                print("diagonal win")
                return True


    # Check negative slopes.
    for row in range(settings.ROWS - (settings.WIN_LENGTH - 1)):
        for col in range(settings.COLS - (settings.WIN_LENGTH - 1)):
            if all(board.iat[row+i, col+i] == token for i in range(settings.WIN_LENGTH)):
                return True

    return False

# Given a line (which will be of length WIN_LENGTH) and a token to check.
    # Will return the calculated score for the PLAYER/AI for that line.
def score_line(line, token):
    score = 0
    oppToken = settings.PLAYER
    if token == settings.PLAYER: oppToken = settings.AI

    # win is worth 1000
    if line.count(token) == settings.WIN_LENGTH:
        return 1000
    if line.count(oppToken) == settings.WIN_LENGTH:
        return -1000
    
    # Line scoring method for multiple WIN_LENGTH possibilities.
    for i in range(2, settings.WIN_LENGTH):
        if line.count(token) == i and line.count(settings.EMPTY) == (settings.WIN_LENGTH - i):
            score += 2*i*i

    if line.count(oppToken) == (settings.WIN_LENGTH - 1) and line.count(settings.EMPTY) == 1:
        score -= 18

    return score

# Function to return the score of a board for a player.
    # This will be the heuristic we use to determine the value of node/board.
def score_board(board, token):
    score = 0

    # Extra score for center column.
    centerCol = list(board.iloc[:, int((settings.COLS - 1)/2)])
    score += 3 * centerCol.count(token)

    # Score horizontals.
    for row in range(settings.ROWS):
        rowLine = list(board.iloc[row, :])
        for col in range(settings.COLS - (settings.WIN_LENGTH - 1)):
            lineSection = rowLine[col: col + settings.WIN_LENGTH]
            score += score_line(lineSection, token)

    # Score verticals.
    for col in range(settings.COLS):
        colLine = list(board.iloc[:, col])
        for row in range(settings.ROWS - (settings.WIN_LENGTH - 1)):
            lineSection = colLine[row: row + settings.WIN_LENGTH]
            score += score_line(lineSection, token)

    # Score positive diagonals.
    for row in range(settings.ROWS - (settings.WIN_LENGTH - 1)):
        for col in range(settings.COLS - (settings.WIN_LENGTH - 1)):
            lineSection = list(board.iloc[row+i, col+i] for i in range(settings.WIN_LENGTH))
            score += score_line(lineSection, token)

    # Score negative diagonals.
    for row in range(settings.ROWS - (settings.WIN_LENGTH - 1)):
        for col in range(settings.COLS - (settings.WIN_LENGTH - 1)):
            lineSection = list(board.iloc[row+(settings.WIN_LENGTH - 1)-i, col+i] for i in range(settings.WIN_LENGTH))
            score += score_line(lineSection, token)

    return score

# Function to check whether a board has a win or is full.
def is_end_node(board):
    return is_win(board, settings.AI) or is_win(board, settings.PLAYER) or (len(all_valid_columns(board)) == 0)


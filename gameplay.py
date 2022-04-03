from board import *
from minimaxAI import *
import random
import math

# How can you have global variables across multiple files?

ROWS = 6
COLS = 7
WIN_LENGTH = 4

EMPTY = 0
PLAYER = 1
AI = 2

PLAYER_TURN = 0
AI_TURN = 1

# Need setup for the board.
    # Create board.
    # Get difficulty level / depth of AI search.
    # Get the number of rows and columns from the user? Or will we manually set those.
    # Randomize the initial starter.

def get_depth():
    depth = input("Choose difficulty between 1 and 5: ")
    print(not(depth.isdigit()))
    if not(depth.isdigit()):
        print("Difficulty selection must be integer. Pick again.")
        return get_depth()

    depth = int(depth)
    if depth > 5 or depth < 1:
        print("Difficulty selection must be between 1 and 5. Pick again.")
        return get_depth()
    
    return depth

def player_turn(board):
    colSelection = input('Choose column between {} and {}: '.format(1, COLS))
    if not(colSelection.isdigit):
        print("Column selection must be integer. Pick again.")
        return player_turn(board)

    colSelection = int(colSelection)
    if colSelection > COLS or colSelection < 0:
        print("Column selection must be within ", range(COLS), "Pick again.")
        return player_turn(board)
    if not is_valid_column(board, colSelection):
        print("Selected column is already full. Pick again.")
        return player_turn(board)

    add_token(board, colSelection, PLAYER)

    return is_win(board, PLAYER)

def AI_turn(board, depth):
    colSelection, score = minimax_alphabeta(board, depth, -math.inf, math.inf, True)

    if is_valid_column(board, colSelection):
        add_token(board, colSelection, AI)

    return is_win(board, AI)

board = create_board_df()
print(board)
depth = get_depth()
turn = random.randint(PLAYER_TURN, AI_TURN)
gameOver = False

# While loop that will continue until game is over.
    # Add option for player to decide whether to start a new game?

# Console version of game.
# ONE SCENARIO AT LEVEL 4 WHERE AI COULD HAVE MADE WINNING MOVE BUT DID NOT.
while not gameOver:
    if turn is PLAYER_TURN:
        gameOver = player_turn(board)
        print(board)
        if gameOver:
            print("PLAYER WINS!")
            break
        turn += 1
        turn = turn % 2
    else:
        gameOver = AI_turn(board, depth)
        print(board)
        if gameOver:
            print("AI WINS!")
            break
        turn += 1
        turn = turn % 2

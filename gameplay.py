from time import sleep
from cv2 import *
from numpy import *
from board import *
from minimaxAI import *
import random
import math
import pygame
import sys
import time
import pandas as pd
from settings import *
from subfile import *
from matplotlib import pyplot as plt

# Initializing global variables in settings.py
initialize_vars(6, 7, 4, 0, 1, 2, 0, 1, 100, int(100/2 -5))

timeTaken_minimax = []
timeTaken_alphabeta = []
predictedMove_minimax = []
predictedMove_alphabeta = []

def get_depth_pygame():
    # prompt the user to select the difficulty level
        # 1 corresponds to shallowest minimax search
        # 5 corresponds to deepest minimax search
    instruct1 = smallFont.render("Select difficulty level using your keyboard.", 1, 'white')
    instruct2 = smallFont.render("Must be between 1 (easiest) and 5 (hardest).", 1, 'white')
    screen.blit(instruct1, (40,10))
    screen.blit(instruct2, (40, 50))
    pygame.display.update()

    # if value entered not between 1 and 5, prompt the user to choose again
    remind = smallFont.render("Difficulty must be between 1 and 5. Choose again.", 1, 'red')
    
    needDepth = True

    while needDepth:
        for event in pygame.event.get():
            # if the user quit, exit the game
            if event.type == pygame.QUIT:
                sys.exit()

            # detect if a key is pressed down
            if event.type == pygame.KEYDOWN:
                needDepth = False # exit the while loop after this iteration
                # set depth to correspond to the player's selection and print their selection to the screen
                if event.key == pygame.K_1:
                    depth = 1
                    decision = smallFont.render("You selected difficulty level 1. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_2:
                    depth = 2
                    decision = smallFont.render("You selected difficulty level 2. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_3:
                    depth = 3
                    decision = smallFont.render("You selected difficulty level 3. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_4:
                    depth = 4
                    decision = smallFont.render("You selected difficulty level 4. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_5:
                    depth = 5
                    decision = smallFont.render("You selected difficulty level 5. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))

                # if the users selection is not valid, print the error message to them
                else:
                    needDepth = True
                    screen.blit(remind, (40,100))
        pygame.display.update() # display the screen

    pygame.time.wait(3000)
    return depth

# function to add a token on the player's turn
def player_turn_pygame(board):
    positionX = event.pos[0] # position of the player's selection
    colSelection = int(math.floor(positionX/settings.SQUARE_SIDE)) # convert the selection to a column
    
    # if the column chosen is valid, add a token to the column
    # otherwise, the player clicked off the screen and can click again
    if is_valid_column(board, colSelection):
        add_token(board, colSelection, settings.PLAYER)

    return

# function to add a token on the AI's turn
def AI_turn(board, depth, moveCount):
    # call function to determine where the AI should play

    # test regular minimax time
    start = time.time()
    colSelection, score = minimax(board, moveCount, depth, True)
    end = time.time()

    predictedMove_minimax.append(colSelection)
    timeTaken_minimax.append(end-start)

    #print('Move Count (minimax):', moveCount)

    # test regular alpha beta pruning
    start = time.time()
    colSelection, score = minimax_alphabeta(board, moveCount, depth, -math.inf, math.inf, True)
    end = time.time()

    predictedMove_alphabeta.append(colSelection)
    timeTaken_alphabeta.append(end-start)
    
    #print('Move Count (alpha-beta):', moveCount)


    # add a token to the selected column
    if is_valid_column(board, colSelection):
        add_token(board, colSelection, settings.AI)

    return (moveCount + 1) # increment moveCount because the AI made a move

# function to display the game board
def print_pygame_board(board):    
    # draw the blue and black game board by looping through each row and column
    for row in range(settings.ROWS):
        for col in range(settings.COLS):
            pygame.draw.rect(screen, 'blue', (col*settings.SQUARE_SIDE, row*settings.SQUARE_SIDE + settings.SQUARE_SIDE, settings.SQUARE_SIDE, settings.SQUARE_SIDE))
            pygame.draw.circle(screen, 'black', (int(col*settings.SQUARE_SIDE + settings.SQUARE_SIDE/2), int(row*settings.SQUARE_SIDE + settings.SQUARE_SIDE + settings.SQUARE_SIDE/2)), settings.RADIUS)

    # add tokens to the proper places, and use the color to correspond to the correct player
    for row in range(settings.ROWS):
        for col in range(settings.COLS):
            if board.iat[row, col] == 1:
                pygame.draw.circle(screen, 'red', (int(col*settings.SQUARE_SIDE + settings.SQUARE_SIDE/2), int(row*settings.SQUARE_SIDE + settings.SQUARE_SIDE + settings.SQUARE_SIDE/2)), settings.RADIUS)
            elif board.iat[row, col] == 2:
                pygame.draw.circle(screen, 'yellow', (int(col*settings.SQUARE_SIDE + settings.SQUARE_SIDE/2), int(row*settings.SQUARE_SIDE + settings.SQUARE_SIDE + settings.SQUARE_SIDE/2)), settings.RADIUS)
    
    pygame.display.update()

board = create_board_df()
turn = random.randint(settings.PLAYER_TURN, settings.AI_TURN) # randomize who starts the game
gameOver = False # set gameOVer to false so the game can be played and the end can later be detected

pygame.init()
screen = pygame.display.set_mode(settings.SCREEN_SIZE)
bigFont = pygame.font.SysFont("arial", 75)
smallFont = pygame.font.SysFont("arial", 35)

depth = get_depth_pygame() # get game depth using function

print_pygame_board(board) # show the board
pygame.display.update()


# While no one has won
while not gameOver:
    moveCount = 0 # initialize moveCount
    for event in pygame.event.get():
        # if the user quit, exit the game
        if event.type == pygame.QUIT:
            sys.exit()

        # update the location of the token to correspond with the user's mouse
        if event.type ==  pygame.MOUSEMOTION:
            # Covers top row with black rectangle.
            pygame.draw.rect(screen, 'black', (0,0, settings.SCREEN_WIDTH, settings.SQUARE_SIDE))
            positionX = event.pos[0] # X position of mouse location
            if turn == settings.PLAYER_TURN:
                # Updates location of Player circle each time the mouse is moved along the top row.
                pygame.draw.circle(screen, 'red', (positionX, int(settings.SQUARE_SIDE/2)), settings.RADIUS)
            
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Covers top row with black rectangle.
            pygame.draw.rect(screen, 'black', (0, 0, settings.SCREEN_WIDTH, settings.SQUARE_SIDE))
            
            if turn == settings.PLAYER_TURN:
                player_turn_pygame(board)
                # if the player won, display a message and end the game
                if is_win(board, settings.PLAYER):
                    label = bigFont.render("Player Wins!", 1, 'red')
                    screen.blit(label, (40,10))
                    gameOver = True

                turn += 1
                turn = turn % 2

                print_pygame_board(board)

    # if it is the AI's turn and the player has not won:
    if turn == settings.AI_TURN and not gameOver:
        moveCount = AI_turn(board, depth, moveCount) # can AI_turn to determine action and place token
        # if the AI won, display a message and end the game
        if is_win(board, settings.AI):
            label = bigFont.render("AI Wins!", 1, 'red')
            screen.blit(label, (40,10))
            gameOver = True

        print_pygame_board(board)

        turn += 1
        turn = turn % 2


def timeAnalysis(minimax, alphabeta):
    
    # Determine sample size (number of moves)
    n = size(minimax)

    # Display Statistics Summary
    minimaxdf = pd.DataFrame(minimax, columns=['Minimax'])
    alphabetadf = pd.DataFrame(alphabeta, columns=['Alpha-Beta'])
    
    print("Minimax mean:", minimaxdf.mean())
    print("Minimax standard deviation:", minimaxdf.std())
    print("Alpha-Beta mean:", alphabetadf.mean())
    print("Alpha-Beta standard deviation:", alphabetadf.std())


    # Create x axis data
    x = np.zeros(n)

    j = 1
    for i in range(n):
        x[i] = i + 1
    
    # Create Plot 
    plt.scatter(x, minimax, label= "Minimax")
    plt.scatter(x, alphabeta, label= "Alpha-Beta")
    plt.legend()
    plt.xlabel("Move Number")
    plt.ylabel("Time (s)")
    plt.title("Time vs Move Number")
    plt.show()
    


# if the game is over pause on the winner message
if gameOver:
    #print('Move Count:', moveCount)

    print("Minimax Times: ", timeTaken_minimax)
    print("Alpha-Beta Times: ", timeTaken_alphabeta)
    
    # Call analysis function
    timeAnalysis(timeTaken_minimax, timeTaken_alphabeta)

    pygame.time.wait(3000)


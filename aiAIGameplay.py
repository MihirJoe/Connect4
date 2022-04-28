from time import sleep
from board import *
from minimaxAI import *
import random
import math
import pygame
import sys
from settings import *
from subfile import *

# Initializing global variables in settings.py
initialize_vars(6, 7, 4, 0, 1, 2, 0, 1, 100, int(100/2 -5))

def get_depth_pygame():
    # prompt the user to select the difficulty level
        # 1 corresponds to shallowest minimax search
        # 5 corresponds to deepest minimax search
    instruct1 = smallFont.render("Select skill level of AI one.", 1, 'white')
    instruct2 = smallFont.render("Must be between 1 (easiest) and 5 (hardest).", 1, 'white')
    instruct3 = smallFont.render("Select skill level of AI two.", 1, 'white')
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
                    depth1 = 1
                    decision = smallFont.render("You selected AI one skill level 1. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_2:
                    depth1 = 2
                    decision = smallFont.render("You selected AI one skill level 2. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_3:
                    depth1 = 3
                    decision = smallFont.render("You selected AI one skill level 3. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_4:
                    depth1 = 4
                    decision = smallFont.render("You selected AI one skill level 4. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))
                elif event.key == pygame.K_5:
                    depth1 = 5
                    decision = smallFont.render("You selected AI one skill level 5. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,150))

                # if the users selection is not valid, print the error message to them
                else:
                    needDepth = True
                    screen.blit(remind, (40,100))
        pygame.display.update() # display the screen

    screen.blit(instruct3, (40,250))
    screen.blit(instruct2, (40, 300))
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
                    depth2 = 1
                    decision = smallFont.render("You selected AI two skill level 1. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,350))
                elif event.key == pygame.K_2:
                    depth2 = 2
                    decision = smallFont.render("You selected AI two skill level 2. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,350))
                elif event.key == pygame.K_3:
                    depth2 = 3
                    decision = smallFont.render("You selected AI two skill level 3. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,350))
                elif event.key == pygame.K_4:
                    depth2 = 4
                    decision = smallFont.render("You selected AI two skill level 4. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,350))
                elif event.key == pygame.K_5:
                    depth2 = 5
                    decision = smallFont.render("You selected AI two skill level 5. Enjoy the game!", 1, 'white')
                    screen.blit(decision, (40,350))

                # if the users selection is not valid, print the error message to them
                else:
                    needDepth = True
                    screen.blit(remind, (40,100))
        pygame.display.update() # display the screen

    pygame.time.wait(3000)
    screen.fill(pygame.Color("black")) 
    return depth1, depth2

# function to add a token on the AI's turn
def AI_turn1(board, depth, moveCount):
    # call function to determine where the AI should play
    colSelection, score = minimax_alphabeta(board, moveCount, depth, -math.inf, math.inf, True, settings.PLAYER, settings.AI)

    # add a token to the selected column
    if is_valid_column(board, colSelection):
        add_token(board, colSelection, settings.PLAYER)

    return (moveCount + 1) # increment moveCount because the AI made a move

def AI_turn2(board, depth, moveCount):
    # call function to determine where the AI should play
    colSelection, score = minimax_alphabeta(board, moveCount, depth, -math.inf, math.inf, True, settings.AI, settings.PLAYER)

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
# let player be AI one and AI be AI two
turn = random.randint(settings.PLAYER_TURN, settings.AI_TURN) # randomize who starts the game
gameOver = False # set gameOVer to false so the game can be played and the end can later be detected

pygame.init()
screen = pygame.display.set_mode(settings.SCREEN_SIZE)
bigFont = pygame.font.SysFont("arial", 75)
smallFont = pygame.font.SysFont("arial", 35)

depth1, depth2 = get_depth_pygame() # get game depth using function

print_pygame_board(board) # show the board
pygame.display.update()


# While no one has won
while not gameOver:
    moveCount1 = 0 # initialize moveCount
    moveCount2 = 0
    for event in pygame.event.get():
        # if the user quit, exit the game
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()

    if turn == settings.PLAYER_TURN and not gameOver:
        moveCount1 = AI_turn1(board, depth1, moveCount1) # call AI_turn to determine action and place token
        # if the AI won, display a message and end the game
        if is_win(board, settings.PLAYER_TURN):
            label = bigFont.render("AI One Wins!", 1, 'red')
            screen.blit(label, (40,10))
            gameOver = True  

        turn += 1
        turn = turn % 2

        print_pygame_board(board)
        pygame.time.wait(3000)


    # if it is the AI's turn and the player has not won:
    if turn == settings.AI_TURN and not gameOver:
        moveCount2 = AI_turn2(board, depth2, moveCount2) # can AI_turn to determine action and place token
        # if the AI won, display a message and end the game
        if is_win(board, settings.AI):
            label = bigFont.render("AI Two Wins!", 1, 'red')
            screen.blit(label, (40,10))
            gameOver = True

        print_pygame_board(board)
        pygame.time.wait(1000)

        turn += 1
        turn = turn % 2

# if the game is over pause on the winner message
    if gameOver:
        pygame.time.wait(3000)


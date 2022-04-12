from time import sleep
from board import *
from minimaxAI import *
import random
import math
import pygame
import sys
from settings import *
from subfile import *

# How can you have global variables across multiple files?
initialize_vars(6, 7, 4, 0, 1, 2, 0, 1, 100, int(100/2 -5))

# Need setup for the board.
    # Create board.
    # Get difficulty level / depth of AI search.
    # Get the number of rows and columns from the user? Or will we manually set those.
    # Randomize the initial starter.

def get_depth_console():
    depth = input("Choose difficulty between 1 and 5: ")
    print(not(depth.isdigit()))
    if not(depth.isdigit()):
        print("Difficulty selection must be integer. Pick again.")
        return get_depth_console()

    depth = int(depth)
    if depth > 5 or depth < 1:
        print("Difficulty selection must be between 1 and 5. Pick again.")
        return get_depth_console()
    
    return depth

def get_depth_pygame():
    instruct1 = smallFont.render("Select difficulty level using your keyboard.", 1, 'white')
    instruct2 = smallFont.render("Must be between 1 (easiest) and 5 (hardest).", 1, 'white')
    screen.blit(instruct1, (40,10))
    screen.blit(instruct2, (40, 50))
    pygame.display.update()

    remind = smallFont.render("Difficulty must be between 1 and 5. Choose again.", 1, 'blue')
    
    needDepth = True

    while needDepth:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                needDepth = False
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
                else:
                    needDepth = True
                    screen.blit(remind, (40,100))
        pygame.display.update()

    pygame.time.wait(3000)
    return depth

def player_turn_console(board):
    colSelection = input('Choose column between {} and {}: '.format(1, settings.COLS))
    if not(colSelection.isdigit):
        print("Column selection must be integer. Pick again.")
        return player_turn_console(board)

    colSelection = int(colSelection)
    if colSelection > settings.COLS or colSelection < 0:
        print("Column selection must be within ", range(settings.COLS), "Pick again.")
        return player_turn_console(board)
    if not is_valid_column(board, colSelection):
        print("Selected column is already full. Pick again.")
        return player_turn_console(board)

    add_token(board, colSelection, settings.PLAYER)

    return is_win(board, settings.PLAYER)

def player_turn_pygame(board):
    positionX = event.pos[0]
    colSelection = int(math.floor(positionX/settings.SQUARE_SIDE))
    
    if is_valid_column(board, colSelection):
        add_token(board, colSelection, settings.PLAYER)

    return

def AI_turn(board, depth):
    moveCount = 0
    colSelection, score = minimax_alphabeta(board, moveCount, depth, -math.inf, math.inf, True)

    if is_valid_column(board, colSelection):
        add_token(board, colSelection, settings.AI)

    return

def print_pygame_board(board):    
    for row in range(settings.ROWS):
        for col in range(settings.COLS):
            pygame.draw.rect(screen, 'blue', (col*settings.SQUARE_SIDE, row*settings.SQUARE_SIDE + settings.SQUARE_SIDE, settings.SQUARE_SIDE, settings.SQUARE_SIDE))
            pygame.draw.circle(screen, 'black', (int(col*settings.SQUARE_SIDE + settings.SQUARE_SIDE/2), int(row*settings.SQUARE_SIDE + settings.SQUARE_SIDE + settings.SQUARE_SIDE/2)), settings.RADIUS)

    for row in range(settings.ROWS):
        for col in range(settings.COLS):
            if board.iat[row, col] == 1:
                pygame.draw.circle(screen, 'red', (int(col*settings.SQUARE_SIDE + settings.SQUARE_SIDE/2), int(row*settings.SQUARE_SIDE + settings.SQUARE_SIDE + settings.SQUARE_SIDE/2)), settings.RADIUS)
            elif board.iat[row, col] == 2:
                pygame.draw.circle(screen, 'yellow', (int(col*settings.SQUARE_SIDE + settings.SQUARE_SIDE/2), int(row*settings.SQUARE_SIDE + settings.SQUARE_SIDE + settings.SQUARE_SIDE/2)), settings.RADIUS)
    
    pygame.display.update()

board = create_board_df()
# depth = get_depth_console()
turn = random.randint(settings.PLAYER_TURN, settings.AI_TURN)
gameOver = False

pygame.init()
screen = pygame.display.set_mode(settings.SCREEN_SIZE)
bigFont = pygame.font.SysFont("arial", 75)
smallFont = pygame.font.SysFont("arial", 35)

depth = get_depth_pygame()

print_pygame_board(board)
pygame.display.update()


# Pygame version of game.
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type ==  pygame.MOUSEMOTION:
            # Covers top row with black rectangle.
            pygame.draw.rect(screen, 'black', (0,0, settings.SCREEN_WIDTH, settings.SQUARE_SIDE))
            positionX = event.pos[0]
            if turn == settings.PLAYER_TURN:
                # Updates location of Player circle each time the mouse is moved along the top row.
                pygame.draw.circle(screen, 'red', (positionX, int(settings.SQUARE_SIDE/2)), settings.RADIUS)
            
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Covers top row with black rectangle.
            pygame.draw.rect(screen, 'black', (0, 0, settings.SCREEN_WIDTH, settings.SQUARE_SIDE))
            
            if turn == settings.PLAYER_TURN:
                player_turn_pygame(board)
                # gameOver = player_turn_console(board)
                # print(board)
                if is_win(board, settings.PLAYER):
                    # print("PLAYER WINS!")
                    label = bigFont.render("Player Wins!", 1, 'red')
                    screen.blit(label, (40,10))
                    gameOver = True
                    print("Game over player wins")

                turn += 1
                turn = turn % 2

                print_pygame_board(board)

                # added so message prints for player
                if gameOver:
                    pygame.time.wait(3000)
                    print("Game over\n")
               

    if turn == settings.AI_TURN and not gameOver:
        AI_turn(board, depth)
        if is_win(board, settings.AI):
            #print("AI WINS!")
            label = bigFont.render("AI Wins!", 1, 'red')
            screen.blit(label, (40,10))
            gameOver = True

        print_pygame_board(board)

        turn += 1
        turn = turn % 2

        if gameOver:
            # pygame.time.wait(3000)
            print("Game over\n")
            sleep(5)

import settings
def initialize_vars(rows, cols, win_length, empty, player, ai,
 player_turn, ai_turn, square_side, radius):
    settings.ROWS = rows
    settings.COLS = cols
    settings.WIN_LENGTH = win_length
    settings.EMPTY = empty
    settings.PLAYER = player
    settings.AI = ai
    settings.PLAYER_TURN = player_turn
    settings.AI_TURN = ai_turn
    settings.SQUARE_SIDE = square_side
    settings.RADIUS = radius
    settings.SCREEN_WIDTH = cols * square_side
    settings.SCREEN_HEIGHT = (rows + 1) * square_side
    settings.SCREEN_SIZE = (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
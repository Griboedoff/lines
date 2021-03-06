# region ExitCodes
QT_NOT_FOUND = 100
# endregion

CELL_SIZE = 60
OUTER_BALL_SIZE = 48
OUTER_BALL_SHIFT = (CELL_SIZE - OUTER_BALL_SIZE) // 2
INNER_BALL_SIZE = 24
INNER_BALL_SHIFT = (CELL_SIZE - INNER_BALL_SIZE) // 2
SCORE_BOARD_SIZE = 3 * CELL_SIZE + 5

# region Colors
# region BallColors
BALL_COLOR_GREEN = (56, 248, 183)
BALL_COLOR_RED = (130, 21, 27)
BALL_COLOR_BLUE = (24, 67, 226)
BALL_COLOR_CYAN = (47, 199, 249)
BALL_COLOR_YELLOW = (228, 230, 52)
BALL_COLOR_MAGENTA = (59, 5, 81)
BALL_COLOR_BROWN = (219, 183, 248)
# endregion

CELL_COLOR = (106, 110, 105)
# endregion

BALL_CHAR_GREEN = "G"
BALL_CHAR_RED = "R"
BALL_CHAR_BLUE = "B"
BALL_CHAR_CYAN = "C"
BALL_CHAR_YELLOW = "Y"
BALL_CHAR_MAGENTA = "M"
BALL_CHAR_BROWN = "W"

CELL_CHAR = '.'

HINT_MODE_MULTIPLIER = {0: 1, 1: 1.5, 2: 2}

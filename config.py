import sys

# region ExitCodes
QT_NOT_FOUND = 100
# endregion

CELL_SIZE = 60
BALL_SIZE = 48
BALL_SHIFT = (CELL_SIZE - BALL_SIZE) // 2
SCORE_BOARD_SIZE = 3 * CELL_SIZE + 5

try:
    from PyQt5.QtGui import QColor
except Exception as e:
    sys.stderr.write('PyQt5 not found: "{}"'.format(e).encode())
    sys.exit(QT_NOT_FOUND)

# region Colors
# region BallColors
BALL_COLOR_GREEN = QColor(56, 248, 183)
BALL_COLOR_RED = QColor(130, 21, 27)
BALL_COLOR_BLUE = QColor(24, 67, 226)
BALL_COLOR_CYAN = QColor(47, 199, 249)
BALL_COLOR_YELLOW = QColor(228, 230, 52)
BALL_COLOR_MAGENTA = QColor(59, 5, 81)
BALL_COLOR_BROWN = QColor(219, 183, 248)
# endregion

CELL_COLOR = QColor(106, 110, 105)
# endregion

HINT_MODE_MULTIPLIER = {0: 1, 1: 1.5, 2: 2}

import enum

import config


class BallColor(enum.Enum):
    GREEN = 0
    RED = 1
    BLUE = 2
    CYAN = 3
    YELLOW = 4
    MAGENTA = 5
    BROWN = 6

    @staticmethod
    def get_qt_color_tuple(ball_color):
        ball_color_match_dict = {
            BallColor.GREEN: config.BALL_COLOR_GREEN,
            BallColor.RED: config.BALL_COLOR_RED,
            BallColor.BLUE: config.BALL_COLOR_BLUE,
            BallColor.CYAN: config.BALL_COLOR_CYAN,
            BallColor.YELLOW: config.BALL_COLOR_YELLOW,
            BallColor.MAGENTA: config.BALL_COLOR_MAGENTA,
            BallColor.BROWN: config.BALL_COLOR_BROWN}
        return ball_color_match_dict[ball_color]

    @staticmethod
    def get_char_repr(ball_color):
        ball_color_match_dict = {
            BallColor.GREEN: config.BALL_CHAR_GREEN,
            BallColor.RED: config.BALL_CHAR_RED,
            BallColor.BLUE: config.BALL_CHAR_BLUE,
            BallColor.CYAN: config.BALL_CHAR_CYAN,
            BallColor.YELLOW: config.BALL_CHAR_YELLOW,
            BallColor.MAGENTA: config.BALL_CHAR_MAGENTA,
            BallColor.BROWN: config.BALL_CHAR_BROWN}
        return ball_color_match_dict[ball_color]


class Ball:
    def __init__(self, color):
        self._colors = {color}

    @property
    def is_multicolor(self):
        return len(self._colors) == 2

    @property
    def colors(self):
        return list(self._colors)

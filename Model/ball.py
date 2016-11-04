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
    def get_color(ball_color):
        ball_color_match_dict = {
            BallColor.GREEN: config.BALL_COLOR_GREEN,
            BallColor.RED: config.BALL_COLOR_RED,
            BallColor.BLUE: config.BALL_COLOR_BLUE,
            BallColor.CYAN: config.BALL_COLOR_CYAN,
            BallColor.YELLOW: config.BALL_COLOR_YELLOW,
            BallColor.MAGENTA: config.BALL_COLOR_MAGENTA,
            BallColor.BROWN: config.BALL_COLOR_BROWN}
        return ball_color_match_dict[ball_color]


class Ball:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return BallColor.get_color(self._color)

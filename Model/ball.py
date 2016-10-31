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
    def get_color(type):
        if type == BallColor.GREEN:
            return config.BALL_COLOR_GREEN
        if type == BallColor.RED:
            return config.BALL_COLOR_RED
        if type == BallColor.BLUE:
            return config.BALL_COLOR_BLUE
        if type == BallColor.CYAN:
            return config.BALL_COLOR_CYAN
        if type == BallColor.YELLOW:
            return config.BALL_COLOR_YELLOW
        if type == BallColor.MAGENTA:
            return config.BALL_COLOR_MAGENTA
        if type == BallColor.BROWN:
            return config.BALL_COLOR_BROWN


class Ball:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return BallColor.get_color(self._color)

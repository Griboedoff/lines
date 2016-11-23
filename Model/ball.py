from typing import List

from Model.ball_color import BallColor


class Ball:
    def __init__(self, colors):
        self._colors = set(colors)

    @property
    def is_multicolor(self) -> bool:
        return len(self._colors) == 2

    @property
    def colors(self) -> List[BallColor]:
        return list(self._colors)

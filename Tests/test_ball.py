import os
import sys
from unittest import TestCase, main

from Model.ball import Ball
from Model.ball_color import BallColor

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestBall(TestCase):
    def setUp(self):
        self.one_color_ball = Ball({BallColor.CYAN})  # type: Ball
        self.multicolor_color_ball = Ball({BallColor.CYAN,
                                           BallColor.BROWN})  # type: Ball

    def test_is_multicolor(self):
        self.assertTrue(self.multicolor_color_ball.is_multicolor)
        self.assertFalse(self.one_color_ball.is_multicolor)

    def test_colors(self):
        self.assertSetEqual(set(self.multicolor_color_ball.colors),
                            {BallColor.CYAN, BallColor.BROWN})
        self.assertSetEqual(set(self.one_color_ball.colors), {BallColor.CYAN})


if __name__ == '__main__':
    main()

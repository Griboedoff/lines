import os
import sys
from unittest import TestCase, main

from Interfaces.controller import Controller
from Model.ball_generator import BallGenerator
from Model.game_field import GameField
from Model.score_board import ScoreBoard

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestBallGenerator(TestCase):
    def test_generate_multicolor_balls(self):
        self.assertTrue(len(list(filter(
            lambda x: x.is_multicolor,
            BallGenerator.generate_balls(100, False, True)))) > 0)

    def test_generate_simple_balls(self):
        self.assertTrue(len(list(filter(
            lambda x: x.is_multicolor,
            BallGenerator.generate_balls(100, False, False)))) == 0)

    def test_generate_n_balls(self):
        self.assertTrue(
            len(BallGenerator.generate_balls(100, False, True)) == 100)

    def test_place_balls(self):
        ball = BallGenerator.generate_balls(1, False, False)
        field = GameField(5)
        controller = Controller(field, ScoreBoard("", {1: 1}, 1), False)
        BallGenerator.place_balls(field, controller, ball)
        self.assertTrue(ball[0] in map(lambda x: x[0], field.balls))


if __name__ == '__main__':
    main()

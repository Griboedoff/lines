from unittest import TestCase

from Interfaces.controller import Controller
from Model.ball_generator import BallGenerator
from Model.game_field import GameField
from Model.score_board import ScoreBoard


class TestBallGenerator(TestCase):
    def test_generate_multicolor_balls(self):
        self.assertTrue(
            len(list(filter(lambda x: x.is_multicolor,
                            BallGenerator.generate_balls(100, True)))) > 0)

    def test_generate_simple_balls(self):
        self.assertTrue(
            len(list(filter(lambda x: x.is_multicolor,
                            BallGenerator.generate_balls(100, False)))) == 0)

    def test_generate_n_balls(self):
        self.assertTrue(len(BallGenerator.generate_balls(100, True)) == 100)

    def test_place_balls(self):
        ball = BallGenerator.generate_balls(1, False)
        field = GameField(5)
        controller = Controller(field, ScoreBoard("", {1: 1}, 1))
        BallGenerator.place_balls(field, controller, ball)
        self.assertTrue(ball[0] in map(lambda x: x[0], field.balls))

from unittest import TestCase

from Interfaces.controller import Controller
from Model.ball import Ball
from Model.ball_color import BallColor
from Model.cell import Cell
from Model.game_field import GameField
from Model.score_board import ScoreBoard


class TestController(TestCase):
    def setUp(self):
        field = GameField(5)
        for i in field.width_r:
            field[(i, 0)] = Cell(Ball({BallColor.BROWN}))
        self.controller = Controller(field,
                                     ScoreBoard("", {"1": 100}, 1))

    def test_current_score(self):
        self.assertTrue(self.controller.current_score == 0)

    def test_show_simple_hint(self):
        self.assertTrue(self.controller.show_simple_hint)

    def test_show_advanced_hint(self):
        self.assertFalse(self.controller.show_advanced_hint)

    def test_is_over(self):
        self.assertFalse(self.controller.is_over)

        self.controller._is_over = True

        self.assertTrue(self.controller.is_over)

    def test_min_score(self):
        self.assertTrue(self.controller.min_score == int(3 ** 1.5 * 1.5))

    def test__perform_move(self):
        self.assertFalse(self.controller.field[1, 1].has_ball)

        self.controller._perform_move((0, 0), (1, 1))

        self.assertTrue(self.controller.field[1, 1].has_ball)

    def test__try_find_and_remove_line(self):
        self.controller._try_find_and_remove_line((0, 0))

        self.assertFalse(len(list(filter(
            lambda x: x,
            (self.controller.field[(i, 0)].has_ball
             for i in self.controller.field.width_r)))))

    def test_find_move_for_hint(self):
        self.controller.field[(1, 1)].ball = Ball({BallColor.BROWN})
        self.controller.field[(3, 3)].ball = Ball({BallColor.BROWN})

        self.assertTrue(self.controller.find_move_for_hint()[1] == (2, 2))

    def test_set_hint_mode(self):
        self.controller.set_hint_mode(0)

        self.assertRaises(self.controller.score_table.hint_mode == 0)

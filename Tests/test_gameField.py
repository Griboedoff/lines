import os
import sys
from unittest import TestCase, main

from Model.ball import Ball
from Model.ball_color import BallColor
from Model.ball_generator import BallGenerator
from Model.cell import Cell
from Model.game_field import GameField

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))


class TestGameField(TestCase):
    def setUp(self):
        self.field = GameField(5)

    def test_width(self):
        self.assertTrue(self.field.width == 5)

    def test_width_r(self):
        self.assertListEqual([i for i in self.field.width_r], [0, 1, 2, 3, 4])

    def test_height(self):
        self.assertTrue(self.field.height == 5)

    def test_height_r(self):
        self.assertListEqual([i for i in self.field.height_r], [0, 1, 2, 3, 4])

    def test_empty_cells_count(self):
        self.assertTrue(self.field.empty_cells_count == 25)

    def test_balls(self):
        self.assertFalse([b for b in self.field.balls])

    def test_is_empty(self):
        self.assertTrue(self.field.is_empty((1, 1)))

    def test_get_set(self):
        coordinates = (1, 1)
        cell = Cell()

        self.field[coordinates] = cell

        self.assertTrue(self.field[coordinates] == cell)
        self.assertRaises(TypeError, self.field.__setitem__(coordinates, cell))

    def test_set_ball(self):
        ball = BallGenerator.generate_balls(1, False)
        coordinates = (1, 1)

        self.field.set_ball(coordinates, ball)

        self.assertTrue(self.field.empty_cells_count == 24)
        self.assertTrue(self.field[coordinates].ball == ball)

    def test_get_completed_lines(self):
        for i in self.field.width_r:
            self.field[(i, 0)] = Cell(Ball({BallColor.BROWN}))

        self.assertTrue(self.field.get_completed_lines((0, 0)))

    def test_find_lines(self):
        for i in self.field.width_r:
            self.field[(i, 0)] = Cell(Ball({BallColor.BROWN}))

        self.assertTrue(len(self.field.find_lines((0, 0))) == 4)

    def test_try_remove_lines(self):
        for i in self.field.width_r:
            self.field[(i, 0)] = Cell(Ball({BallColor.BROWN}))

        self.field.try_remove_lines(self.field.get_completed_lines((0, 0)))

        count = self.field.empty_cells_count
        self.assertTrue(count == 25)

    def test_is_correct_move(self):
        for i in self.field.width_r:
            self.field[(i, 2)] = Cell(Ball({BallColor.BROWN}))
        self.field[(0, 0)] = Cell(Ball({BallColor.RED}))
        self.field[(1, 2)] = Cell(Ball({BallColor.BLUE}))

        self.assertFalse(self.field.is_correct_move((0, 2), (0, 2)))
        self.assertFalse(self.field.is_correct_move((0, 0), (3, 3)))

    def test_perform_move(self):
        ball = Ball({BallColor.RED})
        self.field[(0, 0)] = Cell(ball)

        self.field.perform_move((0, 0), (3, 3))

        self.assertTrue(self.field[(3, 3)].ball == ball)

    def test_is_path_exists(self):
        for i in self.field.width_r:
            self.field[(i, 2)] = Cell(Ball({BallColor.BROWN}))
        self.field[(0, 0)] = Cell(Ball({BallColor.RED}))

        self.assertTrue(self.field.is_path_exists((0, 0), (0, 1)))
        self.assertFalse(self.field.is_path_exists((0, 0), (3, 3)))

    def test_is_in_field(self):
        self.assertFalse(bool(self.field.is_in_field(-1, -1)))
        self.assertTrue(self.field.is_in_field(1, 1))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import os
import sys
from unittest import TestCase

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from Model.ball import Ball
from Model.ball_color import BallColor
from Model.cell import Cell


class TestCell(TestCase):
    def setUp(self):
        self.ball_cell = Cell(Ball({BallColor.RED}))  # type: Cell
        self.cell = Cell()  # type: Cell

    def test_has_ball(self):
        self.assertTrue(self.ball_cell.has_ball)
        self.assertFalse(self.cell.has_ball)

    def test_ball_colors(self):
        self.assertIsNone(self.cell.ball_colors)
        self.assertSetEqual(set(self.ball_cell.ball_colors), {BallColor.RED})

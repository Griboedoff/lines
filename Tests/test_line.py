from unittest import TestCase

from Model.ball_color import BallColor
from Model.line import Line
from Model.lines_types import LineType


class TestLine(TestCase):
    def setUp(self):
        self.line = Line([(2, 2), (1, 1)],
                         LineType.MAIN_DIAGONAL,
                         BallColor.RED)

    def test_start_edge(self):
        self.assertTrue(self.line.start_edge == (3, 3))

    def test_end_edge(self):
        self.assertTrue(self.line.end_edge == (0, 0))

    def test_contains(self):
        self.assertTrue((1, 1) in self.line)

    def test_hash(self):
        l2 = Line([(0, 0)], LineType.VERTICAL, BallColor.BLUE)
        self.assertFalse(hash(l2) == hash(self.line))

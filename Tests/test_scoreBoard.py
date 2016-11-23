from unittest import TestCase

from Model.score_board import ScoreBoard


class TestScoreBoard(TestCase):
    def setUp(self):
        self.board = ScoreBoard("", {"1": 100}, 1)

    def test_set_hint_mode(self):
        self.board.set_hint_mode(2)
        self.assertTrue(self.board.hint_mode == 2)

    def test_update_score(self):
        self.board.update_score(100)
        self.assertTrue(self.board.current_score == 100)

    def test_set_name(self):
        name = "qwe"
        self.board.set_name(name)
        self.assertTrue(name in self.board._score_dict.keys())

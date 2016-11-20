from Model.ball import Ball
from Model.ball_generator import BallGenerator
from Model.game_field import GameField
from Model.score_board import ScoreBoard
from config import HINT_MODE_MULTIPLIER


class Controller:
    def __init__(self, field: GameField, score_table: ScoreBoard):
        self.score_table = score_table
        self.field = field
        self._is_over = False
        self._generate_next_balls()

    @property
    def current_score(self):
        return self.score_table.current_score

    @property
    def show_simple_hint(self):
        return self.score_table._game_mode > 0

    @property
    def show_advanced_hint(self):
        return self.score_table._game_mode > 1

    @property
    def is_over(self):
        return self._is_over

    @property
    def min_score(self):
        return self.calculate_score_for_line(self.field.min_line_length)

    def _perform_move(self, start_pos, finish_pos):
        if (self.field.try_perform_move(start_pos, finish_pos) and
                not self._try_find_and_remove_line(finish_pos)):
            if self.field.empty_cells_count < len(self.next_balls_to_add):
                self._is_over = True
            else:
                BallGenerator.place_balls(self.field,
                                          self,
                                          self.next_balls_to_add)
                self._generate_next_balls()

    def _try_find_and_remove_line(self, coordinates):
        completed_lines = self.field.get_completed_lines(coordinates)
        if completed_lines:
            self.score_table.update_score(
                self.calculate_score_for_line(
                    self.field.try_remove_lines(completed_lines)))
            return True
        return False

    def _generate_next_balls(self):
        self.next_balls_to_add = BallGenerator.generate_balls(
            3, False)
        # (self.score_table.current_score > max(20 * self.min_score,
        #                                       self.score_table.max_score)))

    def add_ball_to_nth_empty_cell(self, n, ball: Ball):
        с = 0
        for x in self.field.width_r:
            for y in self.field.height_r:
                coordinates = (x, y)
                if not self.field[coordinates].has_ball:
                    с += 1
                if n == с:
                    self.field.set_ball(coordinates, ball)
                    self._try_find_and_remove_line(coordinates)
                    return

    def calculate_score_for_line(self, line_length):
        return int(HINT_MODE_MULTIPLIER[
                       self.score_table.game_mode] * line_length ** 1.5)

    def set_game_mode(self, n):
        if not 0 <= n <= 2:
            raise ValueError("hint mode must be from 0 to 2")
        self.score_table.set_game_mode(n)

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
        if self.field.try_perform_move(start_pos, finish_pos):
            completed_lines = self.field.find_lines_length(finish_pos)
            if completed_lines:
                self.score_table.update_score(
                    self.calculate_score_for_line(
                        self.field.try_remove_lines(completed_lines)))
            else:
                if self.field.empty_cells_count < len(self.next_balls_to_add):
                    self._is_over = True
                else:
                    BallGenerator.place_balls(self.field,
                                              self.next_balls_to_add)
                    self._generate_next_balls()

    def _generate_next_balls(self):
        self.next_balls_to_add = BallGenerator.generate_balls(
            3, True)
            # (self.score_table.current_score > max(20 * self.min_score,
            #                                       self.score_table.max_score)))

    def calculate_score_for_line(self, line_length):
        return int(HINT_MODE_MULTIPLIER[
                       self.score_table.game_mode] * line_length ** 1.5)

    def set_game_mode(self, n):
        if not 0 <= n <= 2:
            raise ValueError("hint mode must be from 0 to 2")
        self.score_table.set_game_mode(n)

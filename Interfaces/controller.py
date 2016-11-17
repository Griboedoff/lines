from Model.ball_generator import BallGenerator
from Model.game_field import GameField
from Model.score_table import ScoreTable
from config import HINT_MODE_MULTIPLIER


class Controller:
    def __init__(self, field: GameField, score_table: ScoreTable):
        self.score_table = score_table
        self._game_mode = score_table.game_mode
        self.field = field
        self.next_balls_to_add = BallGenerator.generate_balls(3)
        self._is_over = False

    @property
    def hint_mode(self):
        return self._game_mode == 1

    @property
    def is_over(self):
        return self._is_over

    def handle_move(self, start_pos, finish_pos):
        if self.field.try_perform_move(start_pos, finish_pos):
            completed_lines = self.field.find_lines_length(finish_pos)
            if completed_lines:
                self.score_table.update_score(
                    self.calculate_score_for_line(
                        self.field.try_remove_lines(completed_lines)))
            else:
                if self.field.empty_cells_count < len(self.next_balls_to_add):
                    self._is_over = True
                BallGenerator.place_balls(self.field,
                                          self.next_balls_to_add)
                self.next_balls_to_add = BallGenerator.generate_balls(3)

    def calculate_score_for_line(self, line_length):
        return int(HINT_MODE_MULTIPLIER[self._game_mode] * line_length ** 1.5)

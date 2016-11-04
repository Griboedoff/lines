from Model.ball_generator import BallGenerator
from Model.game_field import GameField
from Model.score_table import ScoreTable
from config import CELL_SIZE, HINT_MODE_MULTIPLIER


class Controller:
    def __init__(self, field: GameField, score_table: ScoreTable):
        self.score_table = score_table
        self._game_mode = score_table.game_mode
        self.field = field
        self._selected_cells = []
        self.next_balls_to_add = BallGenerator.generate_balls(3)

    @property
    def need_to_draw_simple_hint(self):
        return self._game_mode == 1
    @property
    def selected_cell(self):
        if self.has_selected_cell:
            return self._selected_cells[0]

    @property
    def has_selected_cell(self):
        return bool(self._selected_cells)

    def handle_mouse_click(self, mouse_pos):
        coordinates = (mouse_pos.x() // CELL_SIZE, mouse_pos.y() // CELL_SIZE)

        if not self._selected_cells:
            self._selected_cells.append(coordinates)

        elif len(self._selected_cells) == 1:
            self.try_select_second_cell(coordinates)

        if len(self._selected_cells) == 2:
            second_clicked = self._selected_cells.pop()
            first_clicked = self._selected_cells.pop()

            if self.field.try_perform_move(first_clicked, second_clicked):
                completed_lines = self.field.find_lines_length(second_clicked)

                if completed_lines:
                    self.score_table.update_score(
                        self.calculate_score_for_line(
                            self.field.try_remove_lines(completed_lines)))
                else:
                    BallGenerator.place_balls(self.field,
                                              self.next_balls_to_add)
                    self.next_balls_to_add = BallGenerator.generate_balls(3)

    def calculate_score_for_line(self, line_length):
        return int(HINT_MODE_MULTIPLIER[self._game_mode] * (
        line_length * 2))

    def try_select_second_cell(self, coordinates):
        if self.field[coordinates].has_ball:
            self._selected_cells[0] = coordinates
        else:
            self._selected_cells.append(coordinates)

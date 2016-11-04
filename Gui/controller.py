from Model.ball_generator import BallGenerator
from config import CELL_SIZE


class Controller:
    def __init__(self, field):
        self.field = field
        self._selected_cells = []
        self.score = 0
        self.next_balls_to_add = BallGenerator.generate_balls(3)

    @property
    def selected_cell(self):
        if self.has_selected_cell:
            return self._selected_cells[0]

    @property
    def has_selected_cell(self):
        return bool(self._selected_cells)

    def handle_mouse_click(self, pos):
        coordinates = (pos.x() // CELL_SIZE, pos.y() // CELL_SIZE)

        if not self._selected_cells:
            self._selected_cells.append(coordinates)

        elif len(self._selected_cells) == 1:
            self.try_select_second_cell(coordinates)

        if len(self._selected_cells) == 2:
            second_clicked = self._selected_cells.pop()
            first_clicked = self._selected_cells.pop()
            if self.field.try_perform_move(first_clicked, second_clicked):
                completed_lines = self.field.find_lines_length(
                    *second_clicked)
                if completed_lines:
                    self.score += Controller.calculate_score_for_line(
                        self.field.try_remove_lines(completed_lines))
                else:
                    BallGenerator.place_balls(self.field,
                                              self.next_balls_to_add)
                    self.next_balls_to_add = BallGenerator.generate_balls(3)

    @staticmethod
    def calculate_score_for_line(line_length):
        return 0

    def try_select_second_cell(self, coordinates):
        if self.field[coordinates].has_ball:
            self._selected_cells[0] = coordinates
        else:
            self._selected_cells.append(coordinates)

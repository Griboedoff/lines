from Interfaces.controller import Controller
from Model.game_field import GameField
from Model.score_table import ScoreTable
from config import CELL_SIZE


class GuiController(Controller):
    def __init__(self, field: GameField, score_table: ScoreTable):
        super().__init__(field, score_table)
        self._selected_cells = []

    @property
    def selected_cell(self):
        if self.has_selected_cell:
            return self._selected_cells[0]

    @property
    def has_selected_cell(self):
        return bool(self._selected_cells)

    def handle_mouse_click(self, mouse_pos):
        coordinates = (mouse_pos.x() // CELL_SIZE, mouse_pos.y() // CELL_SIZE)
        if not self.field.is_in_field(*coordinates):
            return

        if not self._selected_cells:
            self._selected_cells.append(coordinates)

        elif len(self._selected_cells) == 1:
            self.try_select_second_cell(coordinates)

        if len(self._selected_cells) == 2:
            second_clicked = self._selected_cells.pop()
            first_clicked = self._selected_cells.pop()
            self.handle_move(first_clicked, second_clicked)

    def try_select_second_cell(self, coordinates):
        if self.field[coordinates].has_ball:
            self._selected_cells[0] = coordinates
        else:
            self._selected_cells.append(coordinates)

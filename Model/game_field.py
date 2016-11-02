from Model.cell import Cell
from Model.lines_types import LinesTypes


class GameField:
    def __init__(self):
        self._field = [[Cell() for _ in range(9)] for _ in range(9)]
        self._empty_cells_count = 9 * 9
        self.selected_cell = []

    def __setitem__(self, key, value):
        x, y = key
        if isinstance(value, Cell):
            self._field[x][y] = value
        else:
            raise TypeError("{} in not Cell instance".format(type(value)))

    def __getitem__(self, item):
        x, y = item
        return self._field[x][y]

    # region props
    @property
    def width(self):
        return len(self._field)

    @property
    def width_r(self):
        return range(self.width)

    @property
    def height(self):
        return len(self._field[0])

    @property
    def height_r(self):
        return range(self.height)

    @property
    def get_field(self):
        return self._field

    @property
    def empty_cells_count(self):
        return self._empty_cells_count

    @property
    def has_selected_cell(self):
        return bool(self.selected_cell)

    # endregion

    def add_ball_to_nth_empty_cell(self, n, ball):
        for line in self._field:
            for cell in line:
                if not cell.has_ball:
                    n -= 1
                if n == 0:
                    cell.ball = ball
                    self._empty_cells_count -= 1
                    break

    def check_completed_combination(self, x, y):
        completed_line_types = []
        color = self[x, y].ball_color
        for line_type in LinesTypes:
            c = 0
            for d_v in LinesTypes.get_delta_vectors(line_type):
                i = 1
                current_cell = self[x + d_v[0] * i, y + d_v[1] * i]
                while current_cell.has_ball:
                    if current_cell.ball_color == color:
                        c += 1
                    else:
                        break
                    i += 1
            if c >= 5:
                completed_line_types.append(line_type)
        return completed_line_types

from Model.cell import Cell


class GameField:
    def __init__(self):
        self._field = [[Cell() for _ in range(9)] for _ in range(9)]
        self._empty_cells_count = 9 * 9
        self.selected_cell = []

    # region props
    @property
    def width(self):
        return len(self._field)

    @property
    def width_r(self):
        return range(len(self._field))

    @property
    def height(self):
        return len(self._field[0])

    @property
    def height_r(self):
        return range(len(self._field[0]))

    @property
    def get_field(self):
        return self._field

    @property
    def empty_cells_count(self):
        return self._empty_cells_count

    @property
    def has_selected_cell(self):
        return bool(self.selected_cell)

    # @property
    # def cells_with_balls(self):
    #     return filter(lambda x: x.has_ball, (line for line in self._field))

    # endregion

    def __getitem__(self, item):
        x, y = item
        return self._field[x][y]

    def __setitem__(self, key, value):
        x, y = key
        if isinstance(value, Cell):
            self._field[x][y] = value
        else:
            raise TypeError("{} in not Cell instance".format(type(value)))

    def add_ball_to_nth_empty_cell(self, n, ball):
        for line in self._field:
            for cell in line:
                if not cell.has_ball:
                    n -= 1
                if n == 0:
                    cell.ball = ball
                    self._empty_cells_count -= 1
                    break

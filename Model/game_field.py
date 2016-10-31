from Model.ball_generator import BallGenerator
from Model.cell import Cell


class GameField:
    def __init__(self):
        self._field = [[Cell() for _ in range(9)] for _ in range(9)]
        self._empty_cells_count = 9 * 9

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

    def add_balls(self, count):
        BallGenerator.generate_balls(self, count)

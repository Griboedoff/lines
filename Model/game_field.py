from Model.cell import Cell
from Model.lines_types import LinesTypes


class GameField:
    def __init__(self, field_size=9):

        self._field = [[Cell() for _ in range(field_size)] for _ in
                       range(field_size)]
        self._empty_cells_count = field_size * field_size

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

    # endregion

    def add_ball_to_nth_empty_cell(self, n, ball):
        с = 0
        for line in self._field:
            for cell in line:
                if not cell.has_ball:
                    с += 1
                if n == с:
                    cell.ball = ball
                    self._empty_cells_count -= 1
                    return

    def find_lines_length(self, x, y):
        completed_line_types = []
        color = self[(x, y)].ball_color
        for line_type in LinesTypes:
            line = self._count_same_color_balls_in_line(line_type, x, y, color)
            if len(line) >= (self.width // 2 + 1):
                completed_line_types.append((line_type, line))
        return completed_line_types

    def _count_same_color_balls_in_line(self, line_type, x, y, color):
        line = [(x, y)]
        for d_v in LinesTypes.get_delta_vectors(line_type):
            i = 1
            current_cell_coordinated = (x + d_v[0] * i, y + d_v[1] * i)
            while (self.is_in_field(*current_cell_coordinated) and
                       self[current_cell_coordinated].has_ball):
                if self[current_cell_coordinated].ball_color == color:
                    line.append(current_cell_coordinated)
                else:
                    break
                i += 1
                current_cell_coordinated = (x + d_v[0] * i, y + d_v[1] * i)
        return line

    def try_remove_lines(self, lines):
        if lines:
            longest_line = max(lines, key=lambda x: len(x[1]))
            for coordinates in longest_line[1]:
                self._empty_cells_count -= 1
                self[coordinates] = Cell()
            return len(longest_line[1])

    def try_perform_move(self, start, finish):
        if not self[start].has_ball or start == finish or self[finish].has_ball:
            return False
        is_correct_move = self.is_correct_move(start, finish)
        if is_correct_move:
            self[finish] = self[start]
            self[start] = Cell()
        return is_correct_move

    def is_correct_move(self, start, finish):
        visited = {start}
        st = [start]
        d_coordinates = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while st:
            current = st.pop(0)
            if current == finish:
                return True
            visited.add(current)
            for d_c in d_coordinates:
                neighbour = (current[0] + d_c[0], current[1] + d_c[1])
                if self.is_in_field(*neighbour):
                    has_ball = not self[neighbour].has_ball
                    if has_ball and neighbour not in visited:
                        st.append(neighbour)
        return False

    def is_in_field(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

        # todo handle full field
        # todo tests
        # todo очки, таблица рекордов(11 + 1), имя в конце
        # todo подсказки (что появится следующим, подсказка хода(3/4 очков))
        # todo радужные шарики
        # todo пакетный режим
        # todo nxn поле, шариков (n // 2) + 1

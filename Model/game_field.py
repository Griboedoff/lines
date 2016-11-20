from Model.cell import Cell
from Model.line import Line
from Model.lines_types import LinesTypes


class GameField:
    def __init__(self, field_size: int):
        self._field = [[Cell() for _ in range(field_size)] for _ in
                       range(field_size)]
        self._empty_cells_count = field_size * field_size
        self.min_line_length = self.width // 2 + 1

    def __setitem__(self, key: tuple, value: Cell):
        x, y = key
        if isinstance(value, Cell):
            self._field[x][y] = value
        else:
            raise TypeError("{} in not Cell instance".format(type(value)))

    def __getitem__(self, item: tuple):
        x, y = item
        return self._field[x][y]

    # region props
    @property
    def width(self):
        return len(self._field)

    @property
    def ball_cells(self):
        return filter(self._field)

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
    def balls(self):
        for x in self.width_r:
            for y in self.height_r:
                coordinates = (x, y)
                if self[coordinates].has_ball:
                    yield (self[coordinates].ball, coordinates)

    # endregion

    def is_empty(self, coordinates):
        return self.is_in_field(*coordinates) and not self[coordinates].has_ball

    def set_ball(self, coordinates, ball):
        self[coordinates].ball = ball
        self._empty_cells_count -= 1

    def get_completed_lines(self, coordinates):
        return list(filter(lambda x: len(x) >= self.min_line_length,
                           self.find_lines_length(coordinates)))

    def find_lines_length(self, coordinates: tuple):
        lines = []
        for color in self[coordinates].ball_colors:
            for line_type in LinesTypes:
                lines.append(
                    self._count_same_color_balls_in_line(line_type,
                                                         coordinates,
                                                         color))
        return lines

    def _count_same_color_balls_in_line(self, line_type: LinesTypes,
                                        coordinates, color):
        line = [coordinates]
        place_to_insert = 0
        for d_v in LinesTypes.get_delta_vectors(line_type):
            i = 1
            current_cell_coordinated = (coordinates[0] + d_v[0] * i,
                                        coordinates[1] + d_v[1] * i)
            while (self.is_in_field(*current_cell_coordinated) and
                       self[current_cell_coordinated].has_ball):
                if color not in self[current_cell_coordinated].ball_colors:
                    break
                line.insert(place_to_insert, current_cell_coordinated)
                i += 1
                current_cell_coordinated = (coordinates[0] + d_v[0] * i,
                                            coordinates[1] + d_v[1] * i)
            place_to_insert = -1
        return Line(line, line_type, color)

    def try_remove_lines(self, lines):
        if lines:
            longest_line = max(lines, key=lambda x: len(x))
            for coordinates in longest_line.balls:
                self._empty_cells_count += 1
                self[coordinates] = Cell()
            return len(longest_line)

    def is_correct_move(self, start, finish):
        if not self[start].has_ball or start == finish or self[finish].has_ball:
            return False
        is_correct_move = self.is_path_exists(start, finish)
        return is_correct_move

    def perform_move(self, start, finish):
        self[finish] = self[start]
        self[start] = Cell()

    def is_path_exists(self, start, finish):
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

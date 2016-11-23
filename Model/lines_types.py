import enum


class LineType(enum.Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    MAIN_DIAGONAL = 2
    SECONDARY_DIAGONAL = 3

    @staticmethod
    def get_delta_vectors(line_type):
        line_type_match_dict = {
            LineType.HORIZONTAL: [(1, 0), (-1, 0)],
            LineType.VERTICAL: [(0, 1), (0, -1)],
            LineType.MAIN_DIAGONAL: [(1, 1), (-1, -1)],
            LineType.SECONDARY_DIAGONAL: [(-1, 1), (1, -1)]}
        return line_type_match_dict[line_type]

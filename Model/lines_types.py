import enum


class LinesTypes(enum.Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    MAIN_DIAGONAL = 2
    SECONDARY_DIAGONAL = 3

    @staticmethod
    def get_delta_vectors(line_type):
        line_type_match_dict = {
            LinesTypes.HORIZONTAL: [(1, 0), (-1, 0)],
            LinesTypes.VERTICAL: [(0, 1), (0, -1)],
            LinesTypes.MAIN_DIAGONAL: [(1, 1), (-1, -1)],
            LinesTypes.SECONDARY_DIAGONAL: [(-1, 1), (1, -1)]}
        return line_type_match_dict[line_type]

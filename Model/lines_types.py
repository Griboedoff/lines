import enum


class LinesTypes(enum.Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    MAIN_DIAGONAL = 2
    SECONDARY_DIAGONAL = 3

    @staticmethod
    def get_delta_vectors(type):
        if type == LinesTypes.HORIZONTAL:
            return [(1, 0), (-1, 0)]
        elif type == LinesTypes.VERTICAL:
            return [(0, 1), (0, -1)]
        elif type == LinesTypes.MAIN_DIAGONAL:
            return [(1, 1), (-1, -1)]
        elif type == LinesTypes.SECONDARY_DIAGONAL:
            return [(-1, 1), (1, -1)]
import config
from Model.ball import BallColor
from Model.game_field import GameField


class ConsoleField(GameField):
    def __init__(self, field_size: int):
        super().__init__(field_size)

    def __str__(self):
        res = []
        for x in self.width_r:
            res_s = []
            for y in self.height_r:
                cell = self[(x, y)]
                if not cell.has_ball:
                    res_s.append(config.CELL_CHAR)
                else:
                    if not cell.ball.is_multicolor:
                        res_s.append(
                            BallColor.get_char_repr(cell.ball.colors[0]))
            res.append(''.join(res_s))
        return '\n'.join(res)

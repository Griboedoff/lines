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
                    res_s.append('({})'.format(config.CELL_CHAR * 2))
                else:
                    res_s.append(ConsoleField.get_ball_chars(cell.ball))
            res.append(''.join(res_s))
        return '\n'.join(res)

    @staticmethod
    def get_ball_chars(ball):
        if not ball.is_multicolor:
            return '({})'.format(BallColor.get_char_repr(ball.colors[0]) * 2)
        else:
            return '({})'.format(
                ''.join([BallColor.get_char_repr(c) for c in ball.colors]))

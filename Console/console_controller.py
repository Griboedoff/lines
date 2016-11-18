import re

from Console.console_field import ConsoleField
from Interfaces.controller import Controller
from Model.ball import BallColor
from Model.score_table import ScoreTable

SPLIT_RE = re.compile(r"\s+")
MOVE_ARG_RE = re.compile(r'(?P<x>\d+)\s+(?P<y>\d+)')


class ConsoleController(Controller):
    def __init__(self, field: ConsoleField, score_table: ScoreTable):
        super().__init__(field, score_table)
        self._funcs = {
            "move": self._cmd_move,
            "help": self._cmd_help,
            "score": self._cmd_score,
            "chmod": self._cmd_chmod,
            "show": self._cmd_show,
        }

    def execute(self, cmd: str):
        splitted_cmd = SPLIT_RE.split(cmd)
        if splitted_cmd[0] not in self._funcs.keys():
            raise ValueError(
                "Can't recognize command {}".format(splitted_cmd[0]))
        self._funcs[splitted_cmd[0]](splitted_cmd)

    def _cmd_move(self, cmd):
        first_arg = ' '.join([cmd[1], cmd[2]])
        start_match = MOVE_ARG_RE.match(first_arg)
        second_arg = ' '.join([cmd[3], cmd[4]])
        finish_match = MOVE_ARG_RE.match(second_arg)
        if start_match is None or finish_match is None:
            raise ValueError("Incorrect arguments {}, {} for command 'move'"
                             .format(first_arg, second_arg))
        self._perform_move(self._get_coordinates_from_groupdict(start_match),
                           self._get_coordinates_from_groupdict(finish_match))
        return self._cmd_show('')

    def _get_coordinates_from_groupdict(self, match):
        groupdict = match.groupdict()
        return int(groupdict['x']) - 1, int(groupdict['y']) - 1

    def _cmd_help(self, cmd):
        print(
            """help - displays this message

move <a1> <a2> - move ball from cell <a1> to cell <a2>
    <a1> = <x> <y> - where <x>, <y> int coordinates

score - displays scoreboard

chmod <N> - change hint mode to <N>
    0 - no hint
    1 - simple
    2 - advanced

show - displays field\n""")
        return True

    def _cmd_score(self, cmd):
        print(self.score_table)
        return True

    def _cmd_show(self, cmd):
        next_balls_to_add_ = ("Next balls: " + ''.join(
            BallColor.get_char_repr(ball.colors[0]) for ball in
            self.next_balls_to_add)) if self.show_simple_hint else ''
        print('\n'
              .join([str(self.field),
                     next_balls_to_add_]))
        return True

    def _cmd_chmod(self, cmd):
        try:
            n = int(cmd[1])
        except Exception:
            raise ValueError("Argument must be int, was {}".format(cmd[1]))
        self.set_game_mode(n)
        return True

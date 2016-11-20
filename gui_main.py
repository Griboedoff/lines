#
import argparse
import sys

import config
from Gui.gui_controller import GuiController
from Gui.gui_field import GuiField
from Model.ball_generator import BallGenerator
from Model.game_field import GameField
from Model.score_board import ScoreBoard

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except Exception as e:
    sys.stderr.write('PyQt5 not found: "{}"'.format(e).encode())
    sys.exit(config.QT_NOT_FOUND)


def create_parser():
    """Argument parse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--records', type=str, default='records.txt',
                        help='Path to records table')
    parser.add_argument('-s', '--size', default=9, type=int,
                        help='Game field size')
    parser.add_argument("-h", '--hint-mode', type=int, default=1,
                        help='\n'.join(('Set hints mode:',
                                        '0 - no hints',
                                        '1 - show 3 next balls',
                                        '2 - show one possible move')))
    return parser.parse_args()


if __name__ == '__main__':
    parser = create_parser()

    app = QtWidgets.QApplication(sys.argv)

    game_field = GameField(parser.size)
    controller = GuiController(
        game_field,
        ScoreBoard.load_from(parser.records, parser.mode))
    BallGenerator.place_balls(GameField(parser.size),
                              controller,
                              BallGenerator.generate_balls(10, False))

    ex = GuiField(game_field, controller)

    sys.exit(app.exec_())

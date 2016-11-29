#
import sys

import config
from Gui.gui_controller import GuiController
from Gui.gui_field import GuiField
from Model.ball_generator import BallGenerator
from Model.game_field import GameField
from Model.score_board import ScoreBoard
from utils import create_parser

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except Exception as e:
    sys.stderr.write('PyQt5 not found: "{}"'.format(e).encode())
    sys.exit(config.QT_NOT_FOUND)

if __name__ == '__main__':
    parser = create_parser()

    app = QtWidgets.QApplication(sys.argv)

    game_field = GameField(parser.size)
    controller = GuiController(
        game_field,
        ScoreBoard.load_from(parser.records, parser.hint_mode),
        parser.debug)
    BallGenerator.place_balls(GameField(parser.size),
                              controller,
                              BallGenerator.generate_balls(10, parser.debug,
                                                           False))

    ex = GuiField(game_field, controller)

    sys.exit(app.exec_())

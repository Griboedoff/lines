import sys

import config
from Gui.GuiField import GuiField
from Model.ball_generator import BallGenerator
from Model.game_field import GameField

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except Exception as e:
    print('PyQt5 not found: "{}"'.format(e),
          file=sys.stderr)
    sys.exit(config.QT_NOT_FOUND)


def initialize_game():
    game_field = GameField()
    BallGenerator.generate_balls(game_field, 10)
    return game_field


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    game_field = initialize_game()
    ex = GuiField(game_field)

    sys.exit(app.exec_())

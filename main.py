import sys

import config
from Gui.GuiField import GuiField
from Gui.controller import Controller
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
    BallGenerator.place_balls(game_field, BallGenerator.generate_balls(10))
    return game_field


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    game_field = initialize_game()
    controller = Controller(game_field)
    ex = GuiField(game_field , controller)

    sys.exit(app.exec_())

import sys

import config
from Gui.GuiField import GuiField
from Model.game_field import GameField

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except Exception as e:
    print('PyQt5 not found: "{}"'.format(e),
          file=sys.stderr)
    sys.exit(config.QT_NOT_FOUND)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    field = GameField()
    field.add_balls(10)
    ex = GuiField(field)

    sys.exit(app.exec_())

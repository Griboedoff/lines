import sys

import config

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except Exception as e:
    print('PyQt5 not found: "{}"'.format(e),
          file=sys.stderr)
    sys.exit(config.QT_NOT_FOUND)


class GuiField(QtWidgets.QWidget):
    def __init__(self, field, parent=None):
        super().__init__()
        self.field = field
        self._parent = parent
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 700)
        self.show()

    def paintEvent(self, event):
        painter = QtGui.QPainter()

        painter.begin(self)
        self.draw_field(event, painter)
        painter.end()

    def draw_field(self, event, painter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                self._draw_cell(painter, self.field[(x, y)], x, y)

    def _draw_cell(self, painter, cell, x, y):

        painter.setBrush(config.CELL_COLOR)
        painter.drawRect(x * config.CELL_SIZE, y * config.CELL_SIZE,
                         config.CELL_SIZE, config.CELL_SIZE)

        if cell.has_ball:
            color = cell.ball.color
            painter.setBrush(color)
            painter.drawEllipse(x * config.CELL_SIZE + config.BALL_SHIFT,
                                y * config.CELL_SIZE + config.BALL_SHIFT,
                                config.BALL_SIZE, config.BALL_SIZE)




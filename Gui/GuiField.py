import sys

import config
from config import CELL_SIZE

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

    def mousePressEvent(self, QMouseEvent):
        pos = QMouseEvent.pos()
        self.field.selected_cell = (pos.x() // CELL_SIZE, pos.y() // CELL_SIZE)
        self.repaint()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self._draw_field(event, painter)
        painter.end()

    def _draw_field(self, event, painter):
        self._draw_cells(painter)

        if (self.field.has_selected_cell):
            self._draw_highlighting(painter)

        self._draw_balls(painter)

    def _draw_cells(self, painter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                self._draw_cell(painter, self.field[(x, y)], x, y)

    def _draw_balls(self, painter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                self._draw_ball(painter, x, y)

    def _draw_ball(self, painter, x, y):
        cell = self.field[(x, y)]
        if cell.has_ball:
            color = cell.ball.color
            painter.setBrush(color)
            self._draw_cell_size(painter.drawEllipse,
                                 x, y,
                                 config.BALL_SIZE,
                                 config.BALL_SHIFT)

    def _draw_highlighting(self, painter):
        painter.setPen(QtGui.QColor(255, 255, 0))
        self._draw_cell_size(painter.drawRect,
                             self.field.selected_cell[0],
                             self.field.selected_cell[1])
        painter.setPen(QtGui.QColor(0, 0, 0))

    def _draw_cell(self, painter, cell, x, y):
        painter.setBrush(config.CELL_COLOR)
        self._draw_cell_size(painter.drawRect, x, y)

    def _draw_cell_size(self, painter_func, x, y, obj_size=CELL_SIZE, offset=0):
        painter_func(x * CELL_SIZE + offset,
                     y * CELL_SIZE + offset,
                     obj_size,
                     obj_size)

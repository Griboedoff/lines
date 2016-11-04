import sys

from config import CELL_SIZE, CELL_COLOR, BALL_SIZE, BALL_SHIFT, QT_NOT_FOUND

try:
    from PyQt5 import QtGui, QtCore, QtWidgets
except Exception as e:
    print('PyQt5 not found: "{}"'.format(e),
          file=sys.stderr)
    sys.exit(QT_NOT_FOUND)


class GuiField(QtWidgets.QWidget):
    def __init__(self, field, controller):
        super().__init__()
        self._controller = controller
        self.field = field
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 700, 700)
        self.show()

    def mousePressEvent(self, QMouseEvent):
        self._controller.handle_mouse_click(QMouseEvent.pos())
        self.repaint()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self._draw_field(painter)
        painter.end()

    def _draw_field(self, painter):
        self._draw_cells(painter)

        if self._controller.has_selected_cell:
            self._draw_highlighting(painter)

        self._draw_balls(painter)

    def _draw_cells(self, painter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                self._draw_cell(painter, x, y)

    def _draw_balls(self, painter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                self._draw_ball(painter, x, y)

    def _draw_ball(self, painter, x, y):
        cell = self.field[(x, y)]
        if cell.has_ball:
            color = cell.ball.color
            painter.setBrush(color)
            self._draw_cell_size(painter.drawEllipse, x, y,
                                 BALL_SIZE, BALL_SHIFT)

    def _draw_highlighting(self, painter):
        painter.setPen(QtGui.QColor(255, 255, 0))
        cell = self._controller.selected_cell
        self._draw_cell_size(painter.drawRect, cell[0], cell[1])
        painter.setPen(QtGui.QColor(0, 0, 0))

    def _draw_cell(self, painter, x, y):
        painter.setBrush(CELL_COLOR)
        self._draw_cell_size(painter.drawRect, x, y)

    @staticmethod
    def _draw_cell_size(painter_func, x, y, obj_size=CELL_SIZE, offset=0):
        painter_func(x * CELL_SIZE + offset,
                     y * CELL_SIZE + offset,
                     obj_size, obj_size)

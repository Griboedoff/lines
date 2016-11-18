import sys

from Gui.gui_controller import GuiController
from Model.ball import Ball, BallColor
from Model.game_field import GameField
from config import CELL_COLOR, CELL_SIZE, INNER_BALL_SHIFT, OUTER_BALL_SHIFT, \
    OUTER_BALL_SIZE, QT_NOT_FOUND, SCORE_BOARD_SIZE, INNER_BALL_SIZE

try:
    from PyQt5 import QtGui, QtWidgets, QtCore
except Exception as e:
    print('PyQt5 not found: "{}"'.format(e),
          file=sys.stderr)
    sys.exit(QT_NOT_FOUND)


class GuiField(QtWidgets.QWidget):
    def __init__(self, field: GameField, controller: GuiController):
        super().__init__()
        self._controller = controller
        self.field = field
        self.right_panel_shift = self.field.width * CELL_SIZE + 5
        self.initUI()
        self.resize(self.field.width * CELL_SIZE + SCORE_BOARD_SIZE,
                    self.field.height * CELL_SIZE)

    def initUI(self):
        self.setGeometry(0, 0, 700, 700)
        self.show()

    def mousePressEvent(self, q_mouse_event: QtGui.QMouseEvent):
        self._controller.handle_mouse_click(q_mouse_event.pos())
        self.repaint()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        if self._controller.is_over:
            self._draw_game_end(painter)
            self.close()
        else:
            self._draw_field(painter)
        painter.end()

    def _draw_game_end(self, painter):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("The Game Over")
        msgBox.exec_()

    def _draw_field(self, painter):
        self._draw_cells(painter)

        if self._controller.has_selected_cell:
            self._draw_highlighting(painter)

        self._draw_balls(painter)

        self._draw_score_board(painter)

        if self._controller.show_simple_hint:
            self._draw_simple_hint(painter)

    def _draw_simple_hint(self, painter):
        i = 0
        for ball in self._controller.next_balls_to_add:
            x_shift = self.right_panel_shift + i * CELL_SIZE
            y_shift = (self.field.height - 1) * CELL_SIZE
            self._draw_cell(painter, x_shift, y_shift)
            self._draw_ball(painter, ball, x_shift, y_shift)
            i += 1

    def _draw_score_board(self, painter: QtGui.QPainter):
        painter.drawText(self.right_panel_shift, 0,
                         SCORE_BOARD_SIZE, self.field.height * CELL_SIZE,
                         QtCore.Qt.AlignLeft, str(self._controller.score_table))

    def _draw_cells(self, painter: QtGui.QPainter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                self._draw_cell(painter, x * CELL_SIZE, y * CELL_SIZE)

    def _draw_balls(self, painter: QtGui.QPainter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                cell = self.field[(x, y)]
                if cell.has_ball:
                    self._draw_ball(painter, cell.ball,
                                    x * CELL_SIZE, y * CELL_SIZE)

    @staticmethod
    def _draw_ball(painter, ball: Ball, x, y):
        outer_x = x + OUTER_BALL_SHIFT
        outer_y = y + OUTER_BALL_SHIFT
        painter.setBrush(GuiField.qt_color_from_tuple(
            BallColor.get_qt_color_tuple(ball.colors[0])))
        painter.drawEllipse(outer_x, outer_y,
                            OUTER_BALL_SIZE, OUTER_BALL_SIZE)
        if ball.is_multicolor:
            inner_x = x + INNER_BALL_SHIFT
            inner_y = y + INNER_BALL_SHIFT
            painter.setBrush(GuiField.qt_color_from_tuple(
                BallColor.get_qt_color_tuple(ball.colors[1])))
            painter.drawEllipse(inner_x, inner_y,
                                INNER_BALL_SIZE, INNER_BALL_SIZE)

    def _draw_highlighting(self, painter: QtGui.QPainter):
        painter.setPen(QtGui.QColor(255, 255, 0))
        cell = self._controller.selected_cell
        self._draw_cell(painter, cell[0] * CELL_SIZE, cell[1] * CELL_SIZE)
        painter.setPen(QtGui.QColor(0, 0, 0))

    @staticmethod
    def _draw_cell(painter: QtGui.QPainter, x, y):
        painter.setBrush(GuiField.qt_color_from_tuple(CELL_COLOR))
        painter.drawRect(x, y,
                         CELL_SIZE, CELL_SIZE)

    @staticmethod
    def qt_color_from_tuple(t):
        return QtGui.QColor(*t)

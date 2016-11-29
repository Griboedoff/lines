import sys

from Gui.gui_controller import GuiController
from Model.ball import Ball
from Model.ball_color import BallColor
from Model.game_field import GameField
from config import CELL_COLOR, CELL_SIZE, INNER_BALL_SHIFT, INNER_BALL_SIZE, \
    OUTER_BALL_SHIFT, OUTER_BALL_SIZE, QT_NOT_FOUND, SCORE_BOARD_SIZE

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
        self.cell_size = CELL_SIZE
        self.resize_to_field_size()
        self.right_panel_shift = self.field.width * self.cell_size + 5
        self.initUI()

    def resize_to_field_size(self):
        app = QtCore.QCoreApplication.instance()
        geom = app.desktop().availableGeometry()
        (max_w, max_h) = (geom.width(), geom.height())
        width = self.field.width * self.cell_size + SCORE_BOARD_SIZE
        height = self.field.height * self.cell_size
        if max_w >= width or max_h >= height:
            self.resize(width, height)
            return
        self.show_message_box("The field is bigger than the screen")
        self.exit()

    @staticmethod
    def show_message_box(text):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(text)
        msg_box.exec_()

    def initUI(self):
        self.show()

    def mousePressEvent(self, q_mouse_event: QtGui.QMouseEvent):
        self._controller.handle_mouse_click(q_mouse_event.pos())
        self.repaint()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        if self._controller.is_over:
            self.ask_and_set_name()
            self._draw_game_end()
            self.close()
        else:
            self._draw_field(painter)
        painter.end()

    def ask_and_set_name(self):
        while 1:
            player_name, ok = QtWidgets.QInputDialog.getText(self,
                                                             'Input box',
                                                             'Input your name')
            if ok:
                try:
                    self._controller.score_table.set_name(player_name)
                    self._controller.score_table.save()
                    return
                except Exception as ex:
                    self.show_message_box(ex)

    def _draw_game_end(self):
        self.show_message_box("Game over")

    def _draw_field(self, painter):
        self._draw_cells(painter)

        if self._controller.show_advanced_hint:
            self._draw_advanced_hint(painter)

        if self._controller.has_selected_cell:
            self._draw_highlight(painter, self._controller.selected_cell,
                                 QtGui.QColor(255, 255, 0))

        self._draw_balls(painter)

        self._draw_score_board(painter)

        if self._controller.show_simple_hint:
            self._draw_simple_hint(painter)

    def _draw_simple_hint(self, painter):
        i = 0
        for ball in self._controller.next_balls_to_add:
            x_shift = self.right_panel_shift + i * self.cell_size
            y_shift = (self.field.height - 1) * self.cell_size
            self._draw_cell(painter, x_shift, y_shift)
            self._draw_ball(painter, ball, x_shift, y_shift)
            i += 1

    def _draw_advanced_hint(self, painter):
        move = self._controller.find_move_for_hint()
        if move:
            self._draw_highlight(painter, move[0], QtGui.QColor(0, 255, 0))
            self._draw_highlight(painter, move[1], QtGui.QColor(0, 255, 0))

    def _draw_highlight(self, painter, coordinates, color):
        painter.setPen(color)
        self._draw_cell(painter,
                        coordinates[0] * self.cell_size,
                        coordinates[1] * self.cell_size)
        painter.setPen(QtGui.QColor(0, 0, 0))

    def _draw_score_board(self, painter: QtGui.QPainter):
        painter.drawText(self.right_panel_shift, 0,
                         SCORE_BOARD_SIZE, self.field.height * self.cell_size,
                         QtCore.Qt.AlignLeft, str(self._controller.score_table))

    def _draw_cells(self, painter: QtGui.QPainter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                self._draw_cell(painter, x * self.cell_size, y * self.cell_size)

    def _draw_balls(self, painter: QtGui.QPainter):
        for x in self.field.width_r:
            for y in self.field.height_r:
                cell = self.field[(x, y)]
                if cell.has_ball:
                    self._draw_ball(painter, cell.ball,
                                    x * self.cell_size, y * self.cell_size)

    def _draw_ball(self, painter, ball: Ball, x, y):
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

    def _draw_cell(self, painter: QtGui.QPainter, x, y):
        painter.setBrush(GuiField.qt_color_from_tuple(CELL_COLOR))
        painter.drawRect(x, y,
                         self.cell_size, self.cell_size)

    @staticmethod
    def qt_color_from_tuple(t):
        return QtGui.QColor(*t)

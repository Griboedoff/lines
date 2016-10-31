class Cell:
    def __init__(self, ball = None):
        self.ball = ball

    @property
    def has_ball(self):
        return self.ball != None

    @property
    def ball_color(self):
        if self.has_ball:
            return self.ball.get_color
import math


class Line:
    def __init__(self, balls, type):
        self.balls = balls
        self.type = type
        self.end = balls[-1]
        self.start = balls[0]

    def __len__(self):
        return len(self.balls)

    def __str__(self):
        return 'len= {}, type= {}'.format(len(self), self.type)

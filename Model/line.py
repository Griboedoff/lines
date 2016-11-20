from Model.lines_types import LinesTypes


class Line:
    def __init__(self, balls, line_type, color):
        self.color = color
        self.balls = balls
        self.type = line_type
        self.end = balls[-1]
        self.start = balls[0]

    @property
    def start_edge(self):
        d_v = LinesTypes.get_delta_vectors(self.type)[0]
        return self.start[0] + d_v[0], self.start[1] + d_v[1]

    @property
    def end_edge(self):
        d_v = LinesTypes.get_delta_vectors(self.type)[1]
        return self.end[0] + d_v[0], self.end[1] + d_v[1]

    def __len__(self):
        return len(self.balls)

    def __str__(self):
        return 'len= {}, type= {}'.format(len(self), self.type)

    def __hash__(self):
        return int(self.start[0] ^ 397 + self.start[1]
                   + self.end[0] ^ 397 + self.end[1])

    def __contains__(self, item):
        return item in self.balls

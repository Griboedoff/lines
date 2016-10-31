import random

from Model.ball import Ball, BallColor


class BallGenerator:
    @staticmethod
    def generate_balls(field, ball_number):
        for i in range(ball_number):
            index = random.randint(0, field.empty_cells_count)
            field.add_ball_to_nth_empty_cell(index,
                                             BallGenerator.generate_ball())

    @staticmethod
    def generate_ball():
        return Ball(BallColor(random.randint(0, 6)))

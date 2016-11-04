import random

from Model.ball import Ball, BallColor


class BallGenerator:
    @staticmethod
    def generate_balls(ball_number):
        return [Ball(BallColor(random.randint(0, 6))) for _ in
                range(ball_number)]

    @staticmethod
    def place_balls(field, balls):
        for ball in balls:
            index = random.randint(0, field.empty_cells_count)
            field.add_ball_to_nth_empty_cell(index, ball)

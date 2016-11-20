import random

from Model.ball import Ball, BallColor


class BallGenerator:
    @staticmethod
    def generate_balls(ball_number, with_multicolor):
        generated = []
        if with_multicolor:
            for i in range(ball_number):
                if random.randint(0, 1) % 2 == 0:
                    generated.append(BallGenerator.generate_multicolor())
                else:
                    generated.append(BallGenerator.generate_usual())
            return generated
        else:
            return [BallGenerator.generate_usual() for _ in
                    range(ball_number)]

    @staticmethod
    def generate_multicolor():
        colors = [BallColor(random.randint(0, 3)) for _ in range(2)]
        return Ball(colors)

    @staticmethod
    def generate_usual():
        return Ball([BallColor(random.randint(0, 3))])

    @staticmethod
    def place_balls(field, controller, balls):
        for ball in balls:
            index = random.randint(0, field.empty_cells_count)
            controller.add_ball_to_nth_empty_cell(index, ball)

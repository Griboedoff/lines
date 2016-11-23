import random

from typing import List

from Model.ball import Ball
from Model.ball_color import BallColor


class BallGenerator:
    @staticmethod
    def generate_balls(ball_number, with_multicolor=False) -> List[Ball]:
        generated = []
        if with_multicolor:
            for i in range(ball_number):
                func = random.choice(
                    (BallGenerator._generate_multicolor,
                     BallGenerator._generate_usual))
                generated.append(func())
            return generated
        else:
            return [BallGenerator._generate_usual() for _ in range(ball_number)]

    @staticmethod
    def _generate_multicolor() -> Ball:
        colors = [BallColor(random.randint(0, 6)) for _ in range(2)]
        return Ball(colors)

    @staticmethod
    def _generate_usual() -> Ball:
        return Ball([BallColor(random.randint(0, 6))])

    @staticmethod
    def place_balls(field, controller, balls):
        for ball in balls:
            index = random.randint(0, field.empty_cells_count)
            controller.add_ball_to_nth_empty_cell(index, ball)

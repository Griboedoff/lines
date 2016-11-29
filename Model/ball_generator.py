import random

from typing import List

from Model.ball import Ball
from Model.ball_color import BallColor


class BallGenerator:
    @staticmethod
    def generate_balls(ball_number, debug, with_multicolor=False):
        generated = []
        for i in range(ball_number):
            if debug:
                func = random.choice((BallGenerator._generate_multicolor,
                                      BallGenerator._generate_usual))
            elif with_multicolor:
                if random.randint(0, 10) == 5:
                    func = BallGenerator._generate_multicolor
                else:
                    func = BallGenerator._generate_usual
            else:
                func = BallGenerator._generate_usual
            generated.append(func())
        return generated

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

import argparse
import os

from Console.console_controller import ConsoleController
from Console.console_field import ConsoleField
from Model.ball_generator import BallGenerator
from Model.score_board import ScoreBoard


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def create_parser():
    """Argument parse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--records', type=str, default='records.txt',
                        help='Path to records table')
    parser.add_argument('-s', '--size', default=9, type=int,
                        help='Game field size')
    parser.add_argument("-h", '--hint-mode', type=int, default=1,
                        help='\n'.join(('Set hints mode:',
                                        '0 - no hints',
                                        '1 - show 3 next balls',
                                        '2 - show one possible move')))
    return parser.parse_args()


if __name__ == '__main__':
    parser = create_parser()

    game_field = ConsoleField(parser.size)
    controller = ConsoleController(
        game_field,
        ScoreBoard.load_from(parser.records, parser.mode))
    BallGenerator.place_balls(ConsoleField(parser.size),
                              controller,
                              BallGenerator.generate_balls(10, False))

    cls()
    print("""Hello there!
    to start playing print 'start'
    use 'help' to get other commands

    Good luck!""")
    while not controller.is_over:
        cmd = input()
        cls()
        try:
            started = controller.execute(cmd)
        except Exception as e:
            print(e.args[0] + "\nUse \"help\" for help")

    while 1:
        cls()
        print("""Game Over

        You scored {} points
        Please input your name
        """.format(controller.current_score))
        try:
            controller.score_table.set_name(input())
            break
        except ValueError as e:
            print(e)
    controller.score_table.save()

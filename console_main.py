import os
import sys

from Console.console_controller import ConsoleController
from Console.console_field import ConsoleField
from Model.ball_generator import BallGenerator
from Model.score_board import ScoreBoard
from utils import create_parser


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    parser = create_parser()

    game_field = ConsoleField(parser.size)
    controller = ConsoleController(
        game_field,
        ScoreBoard.load_from(parser.records, parser.hint_mode),
        parser.debug)
    BallGenerator.place_balls(ConsoleField(parser.size),
                              controller,
                              BallGenerator.generate_balls(10, parser.debug,
                                                           False))

    cls()
    print("""Hello there!
    to start playing print 'start'
    use 'help' to get other commands

    Good luck!""")

    while not controller.is_over:
        try:
            run_command(controller)
        except (KeyboardInterrupt, EOFError):
            print("\nTo stop the game type 'exit'")

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


def run_command(controller):
    cmd = input()
    cls()
    try:
        controller.execute(cmd)
    except Exception as e:
        print(e, file=sys.stderr)
        print("Use \"help\" for help", file=sys.stderr)


if __name__ == '__main__':
    main()

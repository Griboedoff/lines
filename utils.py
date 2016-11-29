import argparse


def create_parser():
    """Argument parse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--records', type=str, default='records.txt',
                        help='Path to records table')
    parser.add_argument('-s', '--size', default=9, type=int,
                        help='Game field size')
    parser.add_argument("-m", '--hint-mode', type=int, default=1,
                        help='''Set hints mode:
0 - no hints
1 - show 3 next balls
2 - show one possible move''')
    parser.add_argument('--debug', action='store_true',
                        help='set debug mode on')
    return parser.parse_args()

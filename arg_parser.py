from argparse import ArgumentParser


def parse_args(args):
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Run tests only')
    parser.add_argument('-n', type=int, help='Ordinal number of the Fibonacci number (0-500)')
    parser.add_argument('-a', choices=['N', 'LogN'], help='The algorithm to use')

    args = parser.parse_args(args)

    if not args.test:
        if args.n is None and args.a is None:
            raise ValueError('The program must accept arguments as input: either --test or -a and -n')
        elif args.n is None or args.a is None:
            raise ValueError('-n and -a are required when not using --test')
        elif args.n not in range(501):
            raise ValueError('The value of the -n argument must be between 0 and 500')
    return args

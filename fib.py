from sys import argv
from unittest import TestLoader, TextTestRunner

from arg_parser import parse_args
import fib_algorithms as fa


if __name__ == "__main__":
    args = None
    try:
        args = parse_args(argv[1:])
    except ValueError as e:
        print(f'Error when parse arguments: {e}')
        exit(2)
    if args.test:
        loader = TestLoader()
        suite = loader.discover(start_dir='./tests')
        runner = TextTestRunner()
        runner.run(suite)
    else:
        result = 0
        time = 0
        try:
            if args.a == 'N':
                result, time = fa.fibonacci(args.n, fa.AlgorithmNumber.N.value)
            elif args.a == 'LogN':
                result, time = fa.fibonacci(args.n, fa.AlgorithmNumber.LogN.value)
        except Exception as e:
            print(f'Error when count fibonacci number: {e}')
            exit(1)
        microsecondsInSeconds = 10**6
        print(f'Result: {result}')
        print(f'Time: {time*microsecondsInSeconds:.2f} microseconds')

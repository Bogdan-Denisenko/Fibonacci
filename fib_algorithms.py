from enum import Enum
from time import perf_counter


class AlgorithmNumber(Enum):
    N = 1
    LogN = 2


def fibonacci(n, algorithm_number):

    if type(n) != int:
        raise TypeError("The Fibonacci sequence number must be integer")
    if type(algorithm_number) != int:
        raise TypeError("The algorithm number must be integer")
    if n < 0:
        raise ValueError("The Fibonacci sequence number can't be a negative number")
    if algorithm_number not in list(map(lambda c: c.value, AlgorithmNumber)):
        raise ValueError("Algorithm selected incorrectly, only two algorithms are available - N(1), LogN(2)")

    time = 0
    if n < 2:
        return n, time

    a, b = 1, 1

    if algorithm_number == AlgorithmNumber.N.value:
        start_time = perf_counter()
        for i in range(2, n):
            a, b = b, a + b
        end_time = perf_counter()
        time = end_time - start_time
        return b, time

    elif algorithm_number == AlgorithmNumber.LogN.value:
        start_time = perf_counter()
        for i in range(n.bit_length() - 2, -1, -1):
            tmp_a = a * (2 * b - a)
            tmp_b = b * b + a * a
            a, b = tmp_a, tmp_b
            if (n >> i) & 1:
                a, b = b, a + b
        end_time = perf_counter()
        time = end_time - start_time
        return a, time

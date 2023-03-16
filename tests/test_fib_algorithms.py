from unittest import TestCase

from fib_algorithms import *


class TestFibAlgorithms(TestCase):

    def test_fibonacci_algorithm_N(self):
        n = 10
        expected_result = 55
        result, time = fibonacci(n, AlgorithmNumber.N.value)
        self.assertEqual(result, expected_result)

    def test_fibonacci_algorithm_N_zero(self):
        n = 0
        expected_result = 0
        result, time = fibonacci(n, AlgorithmNumber.N.value)
        self.assertEqual(result, expected_result)

    def test_fibonacci_algorithm_LogN(self):
        n = 10
        expected_result = 55
        result, time = fibonacci(n, AlgorithmNumber.LogN.value)
        self.assertEqual(result, expected_result)

    def test_fibonacci_algorithm_LogN_zero(self):
        n = 0
        expected_result = 0
        result, time = fibonacci(n, AlgorithmNumber.LogN.value)
        self.assertEqual(result, expected_result)

    def test_with_negative_n(self):
        with self.assertRaises(ValueError):
            fibonacci(-1, AlgorithmNumber.LogN.value)

    def test_with_invalid_n(self):
        with self.assertRaises(TypeError):
            fibonacci("string", AlgorithmNumber.LogN.value)
        with self.assertRaises(TypeError):
            fibonacci(1.5, AlgorithmNumber.LogN.value)
        with self.assertRaises(TypeError):
            fibonacci(True, AlgorithmNumber.LogN.value)

    def test_with_non_existent_algorithm(self):
        with self.assertRaises(ValueError):
            fibonacci(1, 3)
        with self.assertRaises(ValueError):
            fibonacci(1, 0)
        with self.assertRaises(ValueError):
            fibonacci(1, -1)

    def test_with_invalid_algorithm(self):
        with self.assertRaises(TypeError):
            fibonacci(1, "string")
        with self.assertRaises(TypeError):
            fibonacci(1, 1.5)
        with self.assertRaises(TypeError):
            fibonacci(1, True)

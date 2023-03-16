from argparse import Namespace
from unittest import TestCase

from arg_parser import parse_args


class TestParseArgs(TestCase):

    def test_parse_args_with_correct_args(self):
        args = parse_args(['--test'])
        self.assertEqual(args, Namespace(test=True, n=None, a=None))

        args = parse_args(['-n', '10', '-a', 'N'])
        self.assertEqual(args, Namespace(test=False, n=10, a='N'))

        args = parse_args(['-n', '10', '-a', 'LogN'])
        self.assertEqual(args, Namespace(test=False, n=10, a='LogN'))

        args = parse_args(['-n', '0', '-a', 'LogN'])
        self.assertEqual(args, Namespace(test=False, n=0, a='LogN'))

        args = parse_args(['-n', '500', '-a', 'N'])
        self.assertEqual(args, Namespace(test=False, n=500, a='N'))

        args = parse_args(['--test', '-n', '1', '-a', 'N'])
        self.assertEqual(args, Namespace(test=True, n=1, a='N'))

    def test_parse_args_without_args(self):
        with self.assertRaises(ValueError):
            parse_args([])

    def test_parse_args_only_with_n(self):
        with self.assertRaises(ValueError):
            parse_args(['-n', '7'])

    def test_parse_args_only_with_a(self):
        with self.assertRaises(ValueError):
            parse_args(['-a', 'LogN'])

    def test_parse_args_with_invalid_upper_n(self):
        with self.assertRaises(ValueError):
            parse_args(['-n', '501', '-a', 'N'])

    def test_parse_args_with_invalid_lower_n(self):
        with self.assertRaises(ValueError):
            parse_args(['-n', '-1', '-a', 'N'])

    def test_parse_args_with_invalid_a(self):
        with self.assertRaises(SystemExit):
            parse_args(['-n', '1', '-a', 'N^2'])

    def test_parse_args_with_non_existent_arg(self):
        with self.assertRaises(SystemExit):
            parse_args(['-n', '1', '-a', 'N', '-l', '3'])

# coding: utf-8
import unittest

from algorithms.math.fibonacci_sequence import fib


class TestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            print(fib(-1))

        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(9), 34)
        self.assertEqual(fib(10), 55)


if __name__ == '__main__':
    unittest.main()

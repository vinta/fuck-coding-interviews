# coding: utf-8
import unittest

from algorithms.math.fibonacci import fib
from algorithms.math.fibonacci import fib_for_loop


class TestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            fib(-1)

        with self.assertRaises(ValueError):
            fib(0.5)

        with self.assertRaises(ValueError):
            fib('abc')

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


class TestCase2(unittest.TestCase):
    def test(self):
        self.assertEqual(fib_for_loop(0), 0)
        self.assertEqual(fib_for_loop(1), 1)
        self.assertEqual(fib_for_loop(2), 1)
        self.assertEqual(fib_for_loop(3), 2)
        self.assertEqual(fib_for_loop(4), 3)
        self.assertEqual(fib_for_loop(5), 5)
        self.assertEqual(fib_for_loop(6), 8)
        self.assertEqual(fib_for_loop(7), 13)
        self.assertEqual(fib_for_loop(8), 21)
        self.assertEqual(fib_for_loop(9), 34)
        self.assertEqual(fib_for_loop(10), 55)

        self.assertEqual(fib_for_loop(100), 354224848179261915075)


if __name__ == '__main__':
    unittest.main()

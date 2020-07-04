# coding: utf-8
"""
F0 = 0
F1 = 1
Fn = Fn-1 + Fn-2
"""
import unittest


def fib(n):
    if n < 0:
        raise ValueError(f'n = {n} is invalid')

    # Base case
    if n <= 1:
        return n

    # Recursive case
    return fib(n - 1) + fib(n - 2)


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

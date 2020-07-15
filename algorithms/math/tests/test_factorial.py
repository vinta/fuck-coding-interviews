# coding: utf-8
import math
import random
import unittest

from algorithms.math.factorial import factorial
from algorithms.math.factorial import factorial_for_loop


class TestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(ValueError):
            factorial(-1)

        with self.assertRaises(ValueError):
            factorial(0.5)

        with self.assertRaises(ValueError):
            factorial('abc')

        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)

    def test_2(self):
        rand_i = random.randint(0, 100)
        self.assertEqual(factorial(rand_i), math.factorial(rand_i))


class TestCase2(unittest.TestCase):
    def test(self):
        self.assertEqual(factorial_for_loop(0), 1)
        self.assertEqual(factorial_for_loop(1), 1)
        self.assertEqual(factorial_for_loop(2), 2)
        self.assertEqual(factorial_for_loop(3), 6)
        self.assertEqual(factorial_for_loop(4), 24)
        self.assertEqual(factorial_for_loop(5), 120)
        self.assertEqual(factorial_for_loop(6), 720)
        self.assertEqual(factorial_for_loop(7), 5040)
        self.assertEqual(factorial_for_loop(8), 40320)
        self.assertEqual(factorial_for_loop(9), 362880)
        self.assertEqual(factorial_for_loop(10), 3628800)

    def test_2(self):
        rand_i = random.randint(0, 10000)
        self.assertEqual(factorial_for_loop(rand_i), math.factorial(rand_i))


if __name__ == '__main__':
    unittest.main()

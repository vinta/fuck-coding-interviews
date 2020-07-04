# coding: utf-8
"""
https://leetcode.com/problems/fibonacci-number/
"""
from functools import lru_cache
import unittest


class Solution:
    @lru_cache()
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        return self.fib(N - 1) + self.fib(N - 2)


class Solution2:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memorize(N)

    def memorize(self, N: int) -> {}:
        caches = {
            0: 0,
            1: 1,
        }

        for i in range(2, N + 1):
            caches[i] = caches[i - 1] + caches[i - 2]

        return caches[N]


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        self.assertEqual(self.solution.fib(0), 0)
        self.assertEqual(self.solution.fib(1), 1)
        self.assertEqual(self.solution.fib(2), 1)
        self.assertEqual(self.solution.fib(3), 2)
        self.assertEqual(self.solution.fib(4), 3)
        self.assertEqual(self.solution.fib(5), 5)
        self.assertEqual(self.solution.fib(6), 8)
        self.assertEqual(self.solution.fib(7), 13)
        self.assertEqual(self.solution.fib(8), 21)
        self.assertEqual(self.solution.fib(9), 34)
        self.assertEqual(self.solution.fib(10), 55)
        self.assertEqual(self.solution.fib(30), 832040)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        self.assertEqual(self.solution.fib(0), 0)
        self.assertEqual(self.solution.fib(1), 1)
        self.assertEqual(self.solution.fib(2), 1)
        self.assertEqual(self.solution.fib(3), 2)
        self.assertEqual(self.solution.fib(4), 3)
        self.assertEqual(self.solution.fib(5), 5)
        self.assertEqual(self.solution.fib(6), 8)
        self.assertEqual(self.solution.fib(7), 13)
        self.assertEqual(self.solution.fib(8), 21)
        self.assertEqual(self.solution.fib(9), 34)
        self.assertEqual(self.solution.fib(10), 55)
        self.assertEqual(self.solution.fib(30), 832040)


if __name__ == '__main__':
    unittest.main()

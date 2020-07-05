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
    caches = {}

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        if (N - 1) not in self.caches:
            self.caches[N - 1] = self.fib(N - 1)

        if (N - 2) not in self.caches:
            self.caches[N - 2] = self.fib(N - 2)

        return self.caches[N - 1] + self.caches[N - 2]


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

# coding: utf-8
"""
https://leetcode.com/problems/fibonacci-number/
"""
from functools import lru_cache


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

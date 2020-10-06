# coding: utf-8
"""
https://leetcode.com/problems/power-of-two/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        if n == 1:
            return True

        while n % 2 == 0:
            n = n / 2
            if n == 1:
                return True

        return False


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n = n / 2
        return True if n == 1 else False


class Solution3:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n & (n - 1) == 0) and (n != 0)

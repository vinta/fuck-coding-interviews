# coding: utf-8
"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution:
    MIN_INT = -2 ** 31
    MAX_INT = 2 ** 31 - 1

    def reverse(self, x: int) -> int:
        reversed_x = int(''.join(reversed(str(abs(x)))))
        if x < 0:
            reversed_x = reversed_x * -1
            if reversed_x < self.MIN_INT:
                return 0
        else:
            if reversed_x > self.MAX_INT:
                return 0
        return reversed_x

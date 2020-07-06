# coding: utf-8
"""
https://leetcode.com/problems/reverse-integer/
"""
import unittest


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


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_lists = [
            (123, 321),
            (120, 21),
            (-123, -321),
            (-120, -21),
            (0, 0),
            (1534236469, 0),
        ]

        for x, expected in test_lists:
            with self.subTest(x=x, expected=expected):
                self.assertEqual(self.solution.reverse(x), expected)


if __name__ == '__main__':
    unittest.main()

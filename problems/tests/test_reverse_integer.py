# coding: utf-8
import unittest

from problems.reverse_integer import Solution


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
            (-2147483648, 0),
        ]

        for x, expected in test_lists:
            with self.subTest(x=x):
                self.assertEqual(self.solution.reverse(x), expected)


if __name__ == '__main__':
    unittest.main()

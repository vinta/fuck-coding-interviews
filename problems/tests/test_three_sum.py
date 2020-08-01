# coding: utf-8
import unittest

from problems.three_sum import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, 0, 1], [-1, -1, 2]]
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test2(self):
        nums = [1, ]
        expected = []
        self.assertEqual(self.solution.threeSum(nums), expected)

    def test3(self):
        nums = [0, 0, 0, 0]
        expected = [[0, 0, 0], ]
        self.assertEqual(self.solution.threeSum(nums), expected)


if __name__ == '__main__':
    unittest.main()

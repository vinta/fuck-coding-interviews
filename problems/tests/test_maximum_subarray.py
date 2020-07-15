# coding: utf-8
import unittest

from problems.maximum_subarray import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxSubArray(nums), 6)


if __name__ == '__main__':
    unittest.main()

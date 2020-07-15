# coding: utf-8
import unittest

from problems.two_sum import Solution
from problems.two_sum import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [2, 3, 7, 11, 15, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 5])


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        nums = [2, 3, 7, 11, 15, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 5])


if __name__ == '__main__':
    unittest.main()

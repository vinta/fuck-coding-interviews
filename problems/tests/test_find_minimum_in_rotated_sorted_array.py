# coding: utf-8
import unittest

from problems.find_minimum_in_rotated_sorted_array import Solution
from problems.find_minimum_in_rotated_sorted_array import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        self.assertEqual(self.solution.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(self.solution.findMin([0, 1, 2, 4, 5, 6, 7]), 0)
        self.assertEqual(self.solution.findMin([1, 2, 4, 5, 6, 7, 0]), 0)
        self.assertEqual(self.solution.findMin([7, 0, 1, 2, 4, 5, 6]), 0)
        self.assertEqual(self.solution.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(self.solution.findMin([1, ]), 1)
        self.assertEqual(self.solution.findMin([2, 1]), 1)
        self.assertEqual(self.solution.findMin([3, 1, 2]), 1)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        self.assertEqual(self.solution.findMin([4, 5, 6, 7, 0, 1, 2]), 0)
        self.assertEqual(self.solution.findMin([0, 1, 2, 4, 5, 6, 7]), 0)
        self.assertEqual(self.solution.findMin([1, 2, 4, 5, 6, 7, 0]), 0)
        self.assertEqual(self.solution.findMin([7, 0, 1, 2, 4, 5, 6]), 0)
        self.assertEqual(self.solution.findMin([3, 4, 5, 1, 2]), 1)
        self.assertEqual(self.solution.findMin([1, ]), 1)
        self.assertEqual(self.solution.findMin([2, 1]), 1)
        self.assertEqual(self.solution.findMin([3, 1, 2]), 1)


if __name__ == '__main__':
    unittest.main()

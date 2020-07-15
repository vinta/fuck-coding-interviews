# coding: utf-8
import unittest

from problems.container_with_most_water import Solution
from problems.container_with_most_water import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(self.solution.maxArea([2, 3, 4, 5, 18, 17, 6]), 17)
        self.assertEqual(self.solution.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 25)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
        self.assertEqual(self.solution.maxArea([2, 3, 4, 5, 18, 17, 6]), 17)
        self.assertEqual(self.solution.maxArea([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 25)


if __name__ == '__main__':
    unittest.main()

# coding: utf-8
import unittest

from problems.contains_duplicate import Solution
from problems.contains_duplicate import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.containsDuplicate(nums), True)

    def test2(self):
        nums = [1, 2, 3]
        self.assertEqual(self.solution.containsDuplicate(nums), False)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.containsDuplicate(nums), True)

    def test2(self):
        nums = [1, 2, 3]
        self.assertEqual(self.solution.containsDuplicate(nums), False)


if __name__ == '__main__':
    unittest.main()

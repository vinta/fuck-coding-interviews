# coding: utf-8
import itertools
import unittest

from problems.permutations import Solution
from problems.permutations import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': []},
            {'nums': [1, ]},
            {'nums': [1, 2]},
            {'nums': [1, 2, 3]},
            {'nums': [1, 2, 3, 4]},
            {'nums': [1, 1, 2, 2, 2]},
        ]
        for data in test_data:
            nums = data['nums']
            expected = itertools.permutations(nums)
            with self.subTest(nums=nums):
                self.assertCountEqual(self.solution.permute(nums), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'nums': []},
            {'nums': [1, ]},
            {'nums': [1, 2]},
            {'nums': [1, 2, 3]},
            {'nums': [1, 2, 3, 4]},
            {'nums': [1, 1, 2, 2, 2]},
        ]
        for data in test_data:
            nums = data['nums']
            output = (tuple(arr) for arr in self.solution.permute(nums))
            expected = itertools.permutations(nums)
            with self.subTest(nums=nums):
                self.assertCountEqual(output, expected)


if __name__ == '__main__':
    unittest.main()

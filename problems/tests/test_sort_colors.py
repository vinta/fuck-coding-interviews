# coding: utf-8
import unittest

from problems.sort_colors import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': [2, 0, 2, 1, 1, 0]},
            {'nums': [2, 0, 1]},
            {'nums': [0, ]},
            {'nums': [1, ]},
            {'nums': []},
        ]
        for data in test_data:
            nums = data['nums']
            expected = sorted(nums.copy())
            with self.subTest(nums=nums):
                self.solution.sortColors(nums)
                self.assertEqual(nums, expected)


if __name__ == '__main__':
    unittest.main()

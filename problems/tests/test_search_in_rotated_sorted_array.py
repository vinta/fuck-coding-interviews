# coding: utf-8
import unittest

from problems.search_in_rotated_sorted_array import Solution
from problems.search_in_rotated_sorted_array import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 0, 'expected': 4},
            {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 3, 'expected': -1},
            {'nums': [3, 5, 7, 9, 11, 1], 'target': 9, 'expected': 3},
            {'nums': [12, 5, 7, 9, 11], 'target': 12, 'expected': 0},
            {'nums': [1, ], 'target': 1, 'expected': 0},
            {'nums': [1, ], 'target': 0, 'expected': -1},
        ]
        for data in test_data:
            nums = data['nums']
            target = data['target']
            expected = data['expected']
            with self.subTest(nums=nums, target=target):
                self.assertEqual(self.solution.search(nums, target), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 0, 'expected': 4},
            {'nums': [4, 5, 6, 7, 0, 1, 2], 'target': 3, 'expected': -1},
            {'nums': [3, 5, 7, 9, 11, 1], 'target': 9, 'expected': 3},
            {'nums': [12, 5, 7, 9, 11], 'target': 12, 'expected': 0},
            {'nums': [1, ], 'target': 1, 'expected': 0},
            {'nums': [1, ], 'target': 0, 'expected': -1},
        ]
        for data in test_data:
            nums = data['nums']
            target = data['target']
            expected = data['expected']
            with self.subTest(nums=nums, target=target):
                self.assertEqual(self.solution.search(nums, target), expected)


if __name__ == '__main__':
    unittest.main()

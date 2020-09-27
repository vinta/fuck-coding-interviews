# coding: utf-8
import unittest

from problems.two_sum import Solution
from problems.two_sum import Solution2
from problems.two_sum import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': [2, 7, 11, 15], 'target': 9, 'expected': [0, 1]},
            {'nums': [3, 2, 4], 'target': 6, 'expected': [1, 2]},
            {'nums': [3, 3], 'target': 6, 'expected': [0, 1]},
            {'nums': [2, 3, 7, 11, 15, 3], 'target': 6, 'expected': [1, 5]},
        ]
        for data in test_data:
            nums = data['nums']
            target = data['target']
            expected = data['expected']
            with self.subTest(nums=nums, target=target, expected=expected):
                self.assertEqual(self.solution.twoSum(nums, target), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'nums': [2, 7, 11, 15], 'target': 9, 'expected': [0, 1]},
            {'nums': [3, 2, 4], 'target': 6, 'expected': [1, 2]},
            {'nums': [3, 3], 'target': 6, 'expected': [0, 1]},
            {'nums': [2, 3, 7, 11, 15, 3], 'target': 6, 'expected': [1, 5]},
        ]
        for data in test_data:
            nums = data['nums']
            target = data['target']
            expected = data['expected']
            with self.subTest(nums=nums, target=target, expected=expected):
                self.assertEqual(self.solution.twoSum(nums, target), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_data = [
            {'nums': [2, 7, 11, 15], 'target': 9, 'expected': [0, 1]},
            {'nums': [3, 2, 4], 'target': 6, 'expected': [1, 2]},
            {'nums': [3, 3], 'target': 6, 'expected': [0, 1]},
            {'nums': [2, 3, 7, 11, 15, 3], 'target': 6, 'expected': [1, 5]},
        ]
        for data in test_data:
            nums = data['nums']
            target = data['target']
            expected = data['expected']
            with self.subTest(nums=nums, target=target, expected=expected):
                self.assertEqual(self.solution.twoSum(nums, target), expected)


if __name__ == '__main__':
    unittest.main()

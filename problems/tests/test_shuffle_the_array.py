# coding: utf-8
import unittest

from problems.shuffle_the_array import Solution
from problems.shuffle_the_array import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': [2, 5, 1, 3, 4, 7], 'n': 3, 'expected': [2, 3, 5, 4, 1, 7]},
            {'nums': [1, 2, 3, 4, 4, 3, 2, 1], 'n': 4, 'expected': [1, 4, 2, 3, 3, 2, 4, 1]},
            {'nums': [1, 1, 2, 2], 'n': 2, 'expected': [1, 2, 1, 2]},
        ]
        for data in test_data:
            nums = data['nums']
            n = data['n']
            expected = data['expected']
            with self.subTest(nums=nums, n=n, expected=expected):
                self.assertEqual(self.solution.shuffle(nums, n), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'nums': [2, 5, 1, 3, 4, 7], 'n': 3, 'expected': [2, 3, 5, 4, 1, 7]},
            {'nums': [1, 2, 3, 4, 4, 3, 2, 1], 'n': 4, 'expected': [1, 4, 2, 3, 3, 2, 4, 1]},
            {'nums': [1, 1, 2, 2], 'n': 2, 'expected': [1, 2, 1, 2]},
        ]
        for data in test_data:
            nums = data['nums']
            n = data['n']
            expected = data['expected']
            with self.subTest(nums=nums, n=n, expected=expected):
                self.assertEqual(self.solution.shuffle(nums, n), expected)


if __name__ == '__main__':
    unittest.main()

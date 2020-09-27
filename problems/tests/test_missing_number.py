# coding: utf-8
import unittest

from problems.missing_number import Solution
from problems.missing_number import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_array = [
            {'nums': [3, 0, 1], 'expected': 2},
            {'nums': [9, 6, 4, 2, 3, 5, 7, 0, 1], 'expected': 8},
        ]
        for data in test_array:
            nums = data['nums']
            expected = data['expected']
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.missingNumber(nums), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_array = [
            {'nums': [3, 0, 1], 'expected': 2},
            {'nums': [9, 6, 4, 2, 3, 5, 7, 0, 1], 'expected': 8},
        ]
        for data in test_array:
            nums = data['nums']
            expected = data['expected']
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.missingNumber(nums), expected)


if __name__ == '__main__':
    unittest.main()

# coding: utf-8
import unittest

from problems.third_maximum_number import Solution
from problems.third_maximum_number import Solution2
from problems.third_maximum_number import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': [3, 2, 1], 'expected': 1},
            {'nums': [1, 2], 'expected': 2},
            {'nums': [1, 1, 2], 'expected': 2},
            {'nums': [2, 2, 3, 1], 'expected': 1},
            {'nums': [2, 2, 2, 2, 2, 2, 3, 1], 'expected': 1},
        ]
        for data in test_data:
            nums = data['nums']
            expected = data['expected']
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.solution.thirdMax(nums), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'nums': [3, 2, 1], 'expected': 1},
            {'nums': [1, 2], 'expected': 2},
            {'nums': [1, 1, 2], 'expected': 2},
            {'nums': [2, 2, 3, 1], 'expected': 1},
            {'nums': [2, 2, 2, 2, 2, 2, 3, 1], 'expected': 1},
        ]
        for data in test_data:
            nums = data['nums']
            expected = data['expected']
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.solution.thirdMax(nums), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_data = [
            {'nums': [3, 2, 1], 'expected': 1},
            {'nums': [1, 2], 'expected': 2},
            {'nums': [1, 1, 2], 'expected': 2},
            {'nums': [2, 2, 3, 1], 'expected': 1},
            {'nums': [2, 2, 2, 2, 2, 2, 3, 1], 'expected': 1},
        ]
        for data in test_data:
            nums = data['nums']
            expected = data['expected']
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.solution.thirdMax(nums), expected)


if __name__ == '__main__':
    unittest.main()

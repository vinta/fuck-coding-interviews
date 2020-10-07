# coding: utf-8
import unittest

from problems.two_sum_ii_input_array_is_sorted import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'numbers': [2, 7, 11, 15], 'target': 9, 'expected': [1, 2]},
            {'numbers': [2, 3, 4], 'target': 6, 'expected': [1, 3]},
            {'numbers': [-1, 0], 'target': -1, 'expected': [1, 2]},
            {'numbers': [1, 2, 3, 4, 5, 6, 7, 19, 100, 222, 412], 'target': 13, 'expected': [6, 7]},
        ]
        for data in test_data:
            numbers = data['numbers']
            target = data['target']
            expected = data['expected']
            with self.subTest(numbers=numbers, target=target, expected=expected):
                self.assertEqual(self.solution.twoSum(numbers, target), expected)


if __name__ == '__main__':
    unittest.main()

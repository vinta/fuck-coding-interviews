# coding: utf-8
import unittest

from problems.find_the_duplicate_number import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        array = [
            {'nums': [1, 3, 4, 2, 2], 'expected': 2},
            {'nums': [3, 1, 3, 4, 2], 'expected': 3},
            {'nums': [1, 1], 'expected': 1},
            {'nums': [1, 1, 2], 'expected': 1},
        ]
        for data in array:
            nums = data['nums']
            expected = data['expected']
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.findDuplicate(nums), expected)


if __name__ == '__main__':
    unittest.main()

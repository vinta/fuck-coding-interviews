# coding: utf-8
import unittest

from problems.single_number import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': [2, 2, 1], 'expected': 1},
            {'nums': [4, 1, 2, 1, 2], 'expected': 4},
        ]
        for data in test_data:
            nums = data['nums']
            expected = data['expected']
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.singleNumber(nums), expected)


if __name__ == '__main__':
    unittest.main()

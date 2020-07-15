# coding: utf-8
import unittest

from problems.product_of_array_except_self import Solution
from problems.product_of_array_except_self import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_output)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        nums = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_output)


if __name__ == '__main__':
    unittest.main()

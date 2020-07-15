# coding: utf-8
import unittest

from problems.maximum_product_subarray import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [2, -5, -2, -4, 3]
        self.assertEqual(self.solution.maxProduct(nums), 24)

    def test2(self):
        nums = [-2, 0, -1]
        self.assertEqual(self.solution.maxProduct(nums), 0)

    def test3(self):
        nums = [3, -1, 4]
        self.assertEqual(self.solution.maxProduct(nums), 4)

    def test4(self):
        nums = [0, 2]
        self.assertEqual(self.solution.maxProduct(nums), 2)


if __name__ == '__main__':
    unittest.main()

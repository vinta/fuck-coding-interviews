# coding: utf-8
"""
https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List
import unittest


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]

        current_product = 1
        for num in nums:
            current_product = current_product * num
            max_product = max(max_product, current_product)

            # when we encounter `0`, the product should be reset
            # however, `0` could still be the maximum product if all other numbers are negative
            if num == 0:
                current_product = 1

        current_product = 1
        for num in reversed(nums):
            current_product = current_product * num
            max_product = max(max_product, current_product, num)

            if num == 0:
                current_product = 1

        return max_product


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

# coding: utf-8
"""
https://leetcode.com/problems/product-of-array-except-self/
"""
from typing import List
import unittest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            product = 1
            for num in nums[0:i] + nums[i + 1:]:
                product = product * num
            output.append(product)

        return output


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = []

        left_products = [1, ] * length
        right_products = [1, ] * length

        for i in range(1, length):
            # start from the second leftmost index to right
            left_products[i] = nums[i - 1] * left_products[i - 1]

            # start from the second rightmost index to left
            right_products[-(i + 1)] = nums[-i] * right_products[-i]

        for i in range(length):
            output.append(left_products[i] * right_products[i])

        return output


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

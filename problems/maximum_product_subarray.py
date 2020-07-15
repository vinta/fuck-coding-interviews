# coding: utf-8
"""
https://leetcode.com/problems/maximum-product-subarray/
"""
from typing import List


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

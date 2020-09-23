# coding: utf-8
"""
https://leetcode.com/problems/shuffle-the-array/
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not n:
            return nums

        def gen_list():
            nums1 = nums[:n]
            nums2 = nums[n:]
            for i, num in enumerate(nums1):
                yield num
                yield nums2[i]

        return list(gen_list())


class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not n:
            return nums

        def gen_list():
            for i in range(n):
                yield nums[i]
                yield nums[n + i]

        return list(gen_list())

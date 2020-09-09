# coding: utf-8
"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[len(sorted_nums) - k]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        kth_largest = None
        for _ in range(k):
            kth_largest = heapq.heappop(max_heap)
        return -kth_largest

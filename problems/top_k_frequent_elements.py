# coding: utf-8
"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        output = []
        for num, _ in counter.most_common(k):
            output.append(num)

        return output

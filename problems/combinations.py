# coding: utf-8
"""
https://leetcode.com/problems/combinations/
"""
from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n + 1)
        return itertools.combinations(nums, k)


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n + 1)
        results = []

        def build_results(items, result):
            if len(result) == k:
                # NOTE: We cannot add `result` directly since it's mutable.
                results.append(result[:])
                return

            for i, item in enumerate(items):
                result.append(item)

                # It's combinations, so we don't need to consider visited items.
                pool_items = items[i + 1:]
                build_results(pool_items, result)

                result.pop()

        build_results(nums, [])
        return results

# coding: utf-8
"""
https://leetcode.com/problems/permutations/
"""
from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutations(elements):
            if len(elements) <= 1:
                yield elements
            else:
                for i, first in enumerate(elements):
                    other_elements = elements[:i] + elements[i + 1:]
                    for permutation in permutations(other_elements):
                        yield [first, ] + permutation

        return permutations(nums)

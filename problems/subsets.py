# coding: utf-8
"""
https://leetcode.com/problems/subsets/
"""
from itertools import combinations
from typing import List
import unittest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(0, len(nums) + 1):
            output.extend([list(p) for p in combinations(nums, i)])

        return output


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def gen_power_set(arr):
            # Base case
            if len(arr) <= 0:
                yield []
            # Recursive case
            else:
                for p in gen_power_set(arr[1:]):
                    yield [arr[0], ] + p
                    yield p

        return list(gen_power_set(nums))


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [1, 2, 3]
        expected = [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test2(self):
        nums = []
        expected = [
            [],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test3(self):
        nums = [1]
        expected = [
            [],
            [1, ],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test4(self):
        nums = [1, 2]
        expected = [
            [],
            [1, ],
            [2, ],
            [1, 2],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        nums = [1, 2, 3]
        expected = [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test2(self):
        nums = []
        expected = [
            [],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test3(self):
        nums = [1]
        expected = [
            [],
            [1, ],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test4(self):
        nums = [1, 2]
        expected = [
            [],
            [1, ],
            [2, ],
            [1, 2],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)


if __name__ == '__main__':
    unittest.main()

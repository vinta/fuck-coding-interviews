# coding: utf-8
"""
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        for i, h in enumerate(height):
            # Find the highest bar on the left side of the current index.
            max_left_h = 0
            for left_h in height[0:i]:
                if left_h > max_left_h:
                    max_left_h = left_h

            # Find the highest bar on the right side of the current index.
            max_right_h = 0
            for right_h in height[i + 1:]:
                if right_h > max_right_h:
                    max_right_h = right_h

            temp_water = min(max_left_h, max_right_h) - h
            if temp_water > 0:
                water += temp_water

        return water

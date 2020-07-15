# coding: utf-8
"""
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i, h1 in enumerate(height):
            for w, h2 in enumerate(height[i + 1:], 1):
                h = min(h1, h2)
                area = w * h
                if area > max_area:
                    max_area = area

        return max_area


class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        # We use two cursors, one starts from the left,
        # another starts from the right
        left = 0
        right = len(height) - 1

        while left < right:
            # The width is fixed in this loop
            ww = right - left

            # The valid area is (width, the smaller height)
            # Since we already found the valid area for the smaller height,
            # the corresponding cursor can move to the next one
            if height[left] < height[right]:
                hh = height[left]
                left = left + 1
            else:
                hh = height[right]
                right = right - 1

            area = ww * hh
            max_area = max(max_area, area)

        return max_area

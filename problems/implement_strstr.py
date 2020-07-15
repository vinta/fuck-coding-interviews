# coding: utf-8
"""
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n_length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + n_length] == needle:
                return i

        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n_length = len(needle)
        h_length = len(haystack)

        if h_length < n_length:
            return -1

        for i in range(h_length - n_length + 1):
            if haystack[i:i + n_length] == needle:
                return i

        return -1

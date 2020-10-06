# coding: utf-8
"""
https://leetcode.com/problems/valid-anagram/
https://algodaily.com/challenges/is-an-anagram
"""
from collections import Counter
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = defaultdict(int)
        for char in s:
            char_counts[char] += 1

        for char in t:
            char_counts[char] -= 1

        for value in char_counts.values():
            if value != 0:
                return False

        return True


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts = defaultdict(int)
        for s_char, t_char in zip(s, t):
            char_counts[s_char] += 1
            char_counts[t_char] -= 1

        for value in char_counts.values():
            if value != 0:
                return False

        return True


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s.lower()) == Counter(t.lower())

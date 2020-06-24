# coding: utf-8
"""
https://leetcode.com/problems/valid-anagram/
"""
from collections import defaultdict
import unittest


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


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = 'anagram'
        t = 'nagaram'
        self.assertEqual(self.solution.isAnagram(s, t), True)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        s = 'anagram'
        t = 'nagaram'
        self.assertEqual(self.solution.isAnagram(s, t), True)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        s = 'anagram'
        t = 'nagaram'
        self.assertEqual(self.solution.isAnagram(s, t), True)


if __name__ == '__main__':
    unittest.main()

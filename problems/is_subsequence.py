# coding: utf-8
"""
https://leetcode.com/problems/is-subsequence/
"""
import unittest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        hits = 0
        start = 0
        for s_c in s:
            for i, t_c in enumerate(t[start:]):
                if s_c == t_c:
                    hits = hits + 1
                    if hits == len(s):
                        return True

                    start = start + i + 1
                    break

        return False


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = 'abc'
        t = 'ahbgdc'
        self.assertEqual(self.solution.isSubsequence(s, t), True)

    def test2(self):
        s = 'bale'
        t = 'abppplee'
        self.assertEqual(self.solution.isSubsequence(s, t), False)

    def test3(self):
        s = ''
        t = ''
        self.assertEqual(self.solution.isSubsequence(s, t), True)


unittest.main()

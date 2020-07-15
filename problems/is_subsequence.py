# coding: utf-8
"""
https://leetcode.com/problems/is-subsequence/
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_len = len(s)
        char_hits = 0
        t_start_index = 0
        for s_char in s:
            for i, t_char in enumerate(t[t_start_index:]):
                if s_char == t_char:
                    char_hits = char_hits + 1
                    if char_hits == s_len:
                        return True

                    # Found the matching character for `s_char`, so break to the next character of `s`
                    # Start from the next index instead of t[0]
                    t_start_index = t_start_index + i + 1
                    break

        return False

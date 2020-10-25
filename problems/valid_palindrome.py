# coding: utf-8
"""
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c for c in s if c.isalnum()).lower()
        # reversed_s = ''.join(reversed(clean_s))
        reversed_s = clean_s[::-1]
        return clean_s == reversed_s


# The Two-Pointer way.
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1

        return True

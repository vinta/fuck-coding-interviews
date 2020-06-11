# coding: utf-8
"""
https://leetcode.com/problems/valid-parentheses/
"""
import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False

        mapping = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']']:
                try:
                    left = stack.pop()
                except IndexError:
                    return False
                right = mapping.get(left)
                if char != right:
                    return False

        if stack:
            return False

        return True


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = '()[]{}'
        self.assertEqual(self.solution.isValid(s), True)

    def test2(self):
        s = '{[]}'
        self.assertEqual(self.solution.isValid(s), True)

    def test3(self):
        s = '([)]'
        self.assertEqual(self.solution.isValid(s), False)

    def test4(self):
        s = '){'
        self.assertEqual(self.solution.isValid(s), False)


unittest.main()

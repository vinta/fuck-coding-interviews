# coding: utf-8
"""
https://leetcode.com/problems/valid-parentheses/
"""


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
            # If we find an opening brace, we push it onto the stack.
            # Having it on the stack means we're waiting to close that particular brace.
            if char in ['(', '{', '[']:
                stack.append(char)
            # If we find a closing brace, we inspect the top element in the stack. We then analyze:
            elif char in [')', '}', ']']:
                # NOTE: The stack might be empty if there are unbalanced brackets.
                try:
                    left = stack.pop()
                except IndexError:
                    return False
                else:
                    if char != mapping[left]:
                        return False

        # If we make it to the end of the line and there's still something left on the stack,
        # that means there’s an opening brace without a corresponding closing brace
        if stack:
            return False

        return True

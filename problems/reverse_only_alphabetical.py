# coding: utf-8
"""
https://algodaily.com/challenges/reverse-only-alphabetical
"""


def reverse_only_alpha(s):
    left = 0
    right = len(s) - 1
    s_list = list(s)
    while left < right:
        if not s_list[left].isalpha():
            left += 1
            continue

        if not s_list[right].isalpha():
            right -= 1
            continue

        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return ''.join(s_list)

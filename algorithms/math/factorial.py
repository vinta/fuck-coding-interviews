# coding: utf-8
"""
https://en.wikipedia.org/wiki/Factorial

0! = 1
1! = 1
n! = n * (n - 1) * (n - 2) * (n - 3) * ... * 3 * 2 * 1
"""


def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('n is invalid')

    # Base case
    if n <= 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


def factorial_for_loop(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i
    return ans

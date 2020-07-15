# coding: utf-8
"""
F0 = 0
F1 = 1
Fn = Fn-1 + Fn-2
"""


def fib(n):
    if n < 0:
        raise ValueError(f'n = {n} is invalid')

    # Base case
    if n <= 1:
        return n

    # Recursive case
    return fib(n - 1) + fib(n - 2)

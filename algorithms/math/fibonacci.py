# coding: utf-8
"""
https://en.wikipedia.org/wiki/Fibonacci_number

fib(0) = 0
fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
"""


def fib(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('n is invalid')

    # Base case
    if n <= 1:
        return n

    # Recursive case
    return fib(n - 1) + fib(n - 2)


def fib_for_loop(n):
    seq = [0, 1]
    for i in range(2, n + 1):
        num = seq[i - 1] + seq[i - 2]
        seq.append(num)

    return seq[n]

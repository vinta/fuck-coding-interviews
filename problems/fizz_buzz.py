# coding: utf-8
"""
https://leetcode.com/problems/fizz-buzz/
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def gen_fizz_buzz(n):
            for num in range(1, n + 1):
                if num % 15 == 0:
                    yield 'FizzBuzz'
                elif num % 3 == 0:
                    yield 'Fizz'
                elif num % 5 == 0:
                    yield 'Buzz'
                else:
                    yield str(num)

        return gen_fizz_buzz(n)

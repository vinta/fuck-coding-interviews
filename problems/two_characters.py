#!/bin/python3
"""
https://www.hackerrank.com/challenges/two-characters/problem
"""
from collections import Counter
import itertools
import os


def alternate(s):
    counter = Counter(s)

    max_length = 0
    for c1, c2 in itertools.combinations(set(s), 2):
        t_length = 0
        is_t_finished = False
        last_char = None
        for char in s:
            if char in (c1, c2):
                # If the total length of `c1` and `c2` is less than the current max length, we don't need to check this combination.
                if (counter[c1] + counter[c2]) <= max_length:
                    break

                # If `char` is the same as `last_char`, the string is not alternating.
                if char == last_char:
                    break

                t_length += 1
                last_char = char
        else:
            # If there is no `break` in this for loop.
            is_t_finished = True

        if is_t_finished and (t_length >= 2):
            max_length = max(max_length, t_length)

    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _ = input()
    s = input()
    result = alternate(s)

    fptr.write(str(result) + '\n')
    fptr.close()

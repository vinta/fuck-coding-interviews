#!/bin/python3
"""
https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
"""
from collections import defaultdict
import os


def hackerrankInString(s):
    target = 'hackerrank'

    char_positions = defaultdict(list)  # {char: [position_index_1, position_index_2, ]}
    for i, char in enumerate(s):
        if char in target:
            char_positions[char].append(i)

    last_index = -1
    for char in target:
        index = None
        for i in char_positions[char]:
            if i > last_index:
                index = i
                break

        if index is None:
            return 'NO'
        else:
            last_index = index

    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    for _ in range(q):
        s = input()
        result = hackerrankInString(s)
        fptr.write(result + '\n')

    fptr.close()

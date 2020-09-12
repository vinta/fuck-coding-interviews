#!/bin/python3
"""
https://www.hackerrank.com/challenges/counting-valleys/problem
"""
import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    mapping = {
        'U': 1,
        'D': -1,
    }
    level = 0
    velley_count = 0
    for walk in path:
        level += mapping[walk]
        if level == 0 and walk == 'U':
            velley_count += 1

    return velley_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()

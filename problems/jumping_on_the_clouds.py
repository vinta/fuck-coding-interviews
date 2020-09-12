#!/bin/python3
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""
import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    steps = 0
    i = 0
    length = len(c)
    while i < length - 1:
        # We can jump by either 1 or 2 clouds.
        if (i + 2) < length:
            if c[i + 2] == 0:
                steps += 1
                i += 2
                continue

        steps += 1
        i += 1

    return steps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()

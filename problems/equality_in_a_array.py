#!/bin/python3
"""
https://www.hackerrank.com/challenges/equality-in-a-array/problem
"""
from collections import Counter
import math
import os
import random
import re
import sys


def equalizeArray(arr):
    counter = Counter(arr)
    delete_count = 0
    for i, data in enumerate(counter.most_common(len(arr))):
        if i == 0:
            continue

        _, count = data
        delete_count += count

    return delete_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = equalizeArray(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

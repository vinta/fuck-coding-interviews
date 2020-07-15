#!/bin/python3
"""
https://www.hackerrank.com/challenges/sock-merchant/problem
"""
import os

from collections import Counter


def sockMerchant(n, ar):
    if n <= 1:
        return 0

    counter = Counter(ar)
    total_pair = 0
    for count in counter.values():
        total_pair += count // 2

    return total_pair

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

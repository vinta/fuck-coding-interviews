#!/bin/python3
"""
https://www.hackerrank.com/challenges/camelcase/problem
"""
import os


def camelcase(s):
    word_count = 0
    for char in s:
        if char.isupper():
            word_count += 1

    if s and s[0].islower():
        word_count += 1

    return word_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = camelcase(s)
    fptr.write(str(result) + '\n')
    fptr.close()

#!/bin/python3
"""
https://www.hackerrank.com/challenges/repeated-string/problem
"""
import math
import os
import random
import re
import sys


def repeatedString(s, n):
    word_length = len(s)
    a_count_in_word = 0
    for char in s:
        if char == 'a':
            a_count_in_word += 1

    # To reach the length of n, the word s at least needs to
    # repeat (n // word_length) times.
    repeated_times = n // word_length
    total_a = repeated_times * a_count_in_word
    for char in s[:n - (repeated_times * word_length)]:
        if char == 'a':
            total_a += 1

    return total_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()

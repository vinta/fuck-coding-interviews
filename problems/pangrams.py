#!/bin/python3
"""
https://www.hackerrank.com/challenges/pangrams/problem
"""
import math
import os
import random
import re
import sys


def pangrams(s):
    alphabet = set()
    for char in s.lower():
        if char != ' ':
            alphabet.add(char)

    if len(alphabet) == 26:
        return 'pangram'
    else:
        return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = pangrams(s)
    fptr.write(result + '\n')
    fptr.close()

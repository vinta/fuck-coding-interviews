# coding: utf-8
"""
https://www.hackerrank.com/challenges/mars-exploration/problem
"""
import os


def marsExploration(s):
    count = 0
    for i in range(0, len(s), 3):  # The length of s will be a multiple of 3.
        if s[i] != 'S':
            count += 1
        if s[i + 1] != 'O':
            count += 1
        if s[i + 2] != 'S':
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = marsExploration(s)
    fptr.write(str(result) + '\n')
    fptr.close()

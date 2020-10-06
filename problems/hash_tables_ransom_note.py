#!/bin/python3
"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""
from collections import Counter


def checkMagazine(magazine, note):
    m_counter = Counter(magazine)
    n_counter = Counter(note)
    for word in note:
        if m_counter.get(word, 0) < n_counter.get(word, 0):
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    checkMagazine(magazine, note)

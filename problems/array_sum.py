# coding: utf-8
"""
https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/array-sum-2-725368ac/description/
"""


def run_solution():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            lines.append(line)

    numbers = [int(num_str) for num_str in lines[1].split()]
    print(sum(numbers))

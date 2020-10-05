#!/bin/python3
"""
https://www.hackerrank.com/challenges/maximum-element/problem
"""
_ = input()  # The total lines.

stack = []
track_stack = []
while True:
    try:
        line = input().split()
    except EOFError:
        break

    if line[0] == '1':  # Push the element x into the stack.
        num = int(line[1])
        stack.append(num)
        try:
            current_max = track_stack[-1]
        except IndexError:
            track_stack.append(num)
        else:
            if num > current_max:
                current_max = num
            track_stack.append(current_max)
    elif line[0] == '2':  # Delete the element present at the top of the stack.
        stack.pop()
        track_stack.pop()
    elif line[0] == '3':  # Print the maximum element in the stack.
        print(track_stack[-1])

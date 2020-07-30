# coding: utf-8
"""
Bubble Sort

Worst-case performance: O(n^2)
Best-case performance: O(n) (the input array is already sorted)
Average performance: O(n^2)
"""


def bubble_sort(arr):
    length = len(arr)

    swapped = True
    while swapped:
        swapped = False

        # We check i and i + 1 in each loop,
        # so we only need length - 1 loops to cover all items
        for i in range(0, length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # We sort one item in each iteration,
        # so the length of remaining unsorted items is reduced by 1
        length = length - 1

    return arr

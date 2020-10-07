# coding: utf-8
"""
Counting Sort
https://en.wikipedia.org/wiki/Counting_sort

Worst-case performance: О(n)
Best-case performance: О(n)
Average performance: О(n)
"""


# NOTE: This implementation can only sort an array which contains only non-negative integers.
def counting_sort(arr, max_num_in_array=None):
    if not arr:
        return arr

    if max_num_in_array is None:
        max_num_in_array = max(arr)

    counts = [0, ] * (max_num_in_array + 1)
    for num in arr:
        counts[num] += 1

    i = 0
    for num, count in enumerate(counts):
        for _ in range(count):
            arr[i] = num
            i += 1

    return arr

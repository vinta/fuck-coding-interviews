# coding: utf-8
"""
Binary Search
https://en.wikipedia.org/wiki/Binary_search_algorithm

Worst-case performance: O(log n)
Best-case performance: O(1)
Average performance: O(log n)

Also see https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/searching/binary_search_left_bound.py
"""


# The following implementations cannot properly handle duplicates.
def binary_search(sorted_array, target):
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == sorted_array[mid]:
            return mid
        elif target < sorted_array[mid]:  # target is on the left side of mid.
            high = mid - 1
        elif target > sorted_array[mid]:  # target is on the right side of mid.
            low = mid + 1

    return -1


def binary_search_recursive(sorted_array, target):
    def binary_search_range(sorted_array, target, low, high):
        # Base case
        if low > high:
            return -1

        # Recursive case
        mid = int((low + high) / 2)
        mid_value = sorted_array[mid]
        if target < mid_value:
            return binary_search_range(sorted_array, target, low, mid - 1)
        elif target > mid_value:
            return binary_search_range(sorted_array, target, mid + 1, high)
        else:
            return mid

    return binary_search_range(sorted_array, target, 0, len(sorted_array) - 1)

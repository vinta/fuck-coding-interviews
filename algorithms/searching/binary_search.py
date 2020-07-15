# coding: utf-8
"""
The following implementations cannot properly handle duplicates.

Also see https://github.com/vinta/fuck-coding-interviews/blob/master/algorithms/searching/binary_search_left_bound.py
"""


def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        mid_value = array[mid]
        if target == mid_value:
            return mid
        elif target < mid_value:
            high = mid - 1
        elif target > mid_value:
            low = mid + 1

    return -1


def binary_search_recursive(array, target):
    def binary_search_range(array, target, low, high):
        # Base case
        if low > high:
            return -1

        # Recursive case
        mid = int((low + high) / 2)
        mid_value = array[mid]
        if target < mid_value:
            return binary_search_range(array, target, low, mid - 1)
        elif target > mid_value:
            return binary_search_range(array, target, mid + 1, high)
        else:
            return mid

    return binary_search_range(array, target, 0, len(array) - 1)

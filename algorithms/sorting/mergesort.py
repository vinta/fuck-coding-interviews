# coding: utf-8
"""
Merge Sort
https://en.wikipedia.org/wiki/mergesort

Worst-case performance: O(n * log n)
Best-case performance: O(n * log n)
Average performance: O(n * log n)
"""


# We could replace this function with `heapq.merge()`.
def merge(sorted_arr1, sorted_arr2):
    sorted_arr = []
    i1 = 0
    i2 = 0
    while True:
        # Since there is no item to process in `sorted_arr1`,
        # we simply merge the remainder of `sorted_arr2` into the result.
        try:
            current1 = sorted_arr1[i1]
        except IndexError:
            sorted_arr.extend(sorted_arr2[i2:])  # NOTE: Only merge the remainder.
            break

        try:
            current2 = sorted_arr2[i2]
        except IndexError:
            sorted_arr.extend(sorted_arr1[i1:])
            break

        if current1 <= current2:
            sorted_arr.append(current1)
            i1 += 1
        else:
            sorted_arr.append(current2)
            i2 += 1

    return sorted_arr


def mergesort(arr):
    # Base case:
    # The list is considered sorted if it's empty or there is only one item.
    if len(arr) <= 1:
        return arr

    # Recursive case:
    # Divide the list in half, sort both sublists recursively, then merge two sorted lists.
    middle_index = len(arr) // 2
    sorted_left_list = mergesort(arr[:middle_index])
    sorted_right_list = mergesort(arr[middle_index:])
    return merge(sorted_left_list, sorted_right_list)

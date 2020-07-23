# coding: utf-8


def linear_search(array, target):
    for i, item in enumerate(array):
        if item == target:
            return i

    return -1

# coding: utf-8
import heapq

from data_structures.heaps.array_based_binary_heap import ArrayBasedBinaryHeap


def heap_sort(arr):
    heap = ArrayBasedBinaryHeap()
    for item in arr:
        heap.push(item)
    return [heap.pop_min() for _ in range(len(arr))]


def heap_sort_heapq(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

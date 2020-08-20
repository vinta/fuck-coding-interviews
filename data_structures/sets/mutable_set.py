# coding: utf-8
from collections.abc import MutableSet, Sequence

from algorithms.hashing.mad_compression import mad


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/hash_maps/chain_hash_map.py
# This implementation is very similar to ChainHashMap.
class Set(MutableSet):
    def __init__(self, elems=None, capacity=None, lf_threshold=None):
        self._bucket_array = [None, ] * (capacity if capacity else 11)
        self._size = 0
        self._load_factor_threshold = lf_threshold if lf_threshold else 0.5

        elems = elems if isinstance(elems, Sequence) else []
        for elem in elems:
            self.add(elem)

    # O(1)
    def __len__(self):
        return self._size

    # O(n)
    def __iter__(self):
        for bucket in self._bucket_array:
            if bucket:
                for elem in bucket:
                    yield elem

    # O(1) + O(fairly small n) for linear searching if the load factor is below 1
    def __contains__(self, elem):
        i = self._hash_func(elem)
        bucket = self._bucket_array[i]
        if bucket:
            for _elem in bucket:
                if _elem == elem:
                    return True
        return False

    # O(1)
    def _hash_func(self, key):
        return mad(hash(key), len(self._bucket_array))

    # O(1)
    def _load_factor(self):
        return self._size / len(self._bucket_array)

    # O(n)
    def _resize(self, new_capacity):
        old_bucket_array = self._bucket_array[:]
        self._bucket_array = [None, ] * new_capacity
        self._size = 0
        for bucket in old_bucket_array:
            if bucket:
                for elem in bucket:
                    self.add(elem)

    def _auto_resize(self):
        if self._load_factor() > self._load_factor_threshold:
            self._resize(len(self._bucket_array) * 2 - 1)

    # O(1) + O(fairly small n) for linear searching if the load factor is below 1
    # O(n) if it triggers resizing
    def add(self, elem):
        i = self._hash_func(elem)
        if self._bucket_array[i] is None:
            self._bucket_array[i] = []

        if elem not in self._bucket_array[i]:
            self._bucket_array[i].append(elem)
            self._size += 1
            self._auto_resize()

    # O(1) + O(fairly small n) for linear searching if the load factor is below 1
    def discard(self, elem):
        i = self._hash_func(elem)
        bucket = self._bucket_array[i]
        if bucket:
            for j in range(len(bucket)):
                if bucket[j] == elem:
                    bucket.remove(elem)
                    self._size -= 1
                    return

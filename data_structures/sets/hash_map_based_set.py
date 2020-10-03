# coding: utf-8
"""
Set
https://en.wikipedia.org/wiki/Set_(abstract_data_type)
https://www.geeksforgeeks.org/internal-working-of-set-in-python/
"""
from collections.abc import MutableSet, Sequence

from algorithms.hashing.mad_compression import mad


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/hash_maps/chain_hash_map.py
# This implementation is very similar to ChainHashMap,
# but it doesn't need the nested UnsortedTableMap to store the value.
class SimpleHashMap:
    def __init__(self, capacity=None, lf_threshold=None, dummy_value=1):
        self._buckets = [None, ] * (capacity if capacity else 11)
        self._size = 0
        self._load_factor_threshold = lf_threshold if lf_threshold else 0.5
        self._dummy_value = dummy_value

    def __len__(self):
        return self._size

    def __iter__(self):
        for bucket in self._buckets:
            if bucket:
                for elem in bucket:
                    yield elem

    def __contains__(self, elem):
        i = self._hash_func(elem)
        bucket = self._buckets[i]
        if bucket:
            for _elem in bucket:
                if _elem == elem:
                    return True
        return False

    def _hash_func(self, key):
        return mad(hash(key), len(self._buckets))

    def _load_factor(self):
        return self._size / len(self._buckets)

    def _resize(self, new_capacity):
        old_buckets = self._buckets[:]
        self._buckets = [None, ] * new_capacity
        self._size = 0
        for bucket in old_buckets:
            if bucket:
                for elem in bucket:
                    self[elem] = self._dummy_value  # Re-hash old keys.

    def _auto_resize(self):
        if self._load_factor() > self._load_factor_threshold:
            self._resize(len(self._buckets) * 2 - 1)

    def __setitem__(self, key, value):
        i = self._hash_func(key)
        if self._buckets[i] is None:
            self._buckets[i] = []  # We don't need to store the dummy value.

        if key not in self._buckets[i]:  # Prevent duplicates.
            self._buckets[i].append(key)
            self._size += 1
            self._auto_resize()

    def __delitem__(self, key):
        i = self._hash_func(key)
        bucket = self._buckets[i]
        if bucket:
            for j, _key in enumerate(bucket):
                if _key == key:
                    bucket.pop(j)
                    self._size -= 1
                    return
        else:
            raise KeyError


class Set(MutableSet):
    def __init__(self, elems=None, capacity=None, lf_threshold=None):
        self._dummy_value = 1
        self._hash_map = SimpleHashMap(capacity, lf_threshold, self._dummy_value)

        elems = elems if isinstance(elems, Sequence) else []
        for elem in elems:
            self.add(elem)

    # O(1)
    def __len__(self):
        return len(self._hash_map)

    # O(n)
    def __iter__(self):
        return self._hash_map.__iter__()

    # O(1) + O(fairly small n) for linear searching if the load factor is below 1
    def __contains__(self, elem):
        return self._hash_map.__contains__(elem)

    # O(1) + O(fairly small n) for linear searching if the load factor is below 1
    # O(n) if it triggers resizing
    def add(self, elem):
        self._hash_map[elem] = self._dummy_value

    # O(1) + O(fairly small n) for linear searching if the load factor is below 1
    def discard(self, elem):
        try:
            del self._hash_map[elem]
        except KeyError:
            pass

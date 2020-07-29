# coding: utf-8
"""
ChainHashMap uses Separate Chaining as collision resolution strategy.

https://en.wikipedia.org/wiki/Hash_table#Separate_chaining
"""
import statistics

from data_structures.hash_maps.base_map import BaseHashMap
from data_structures.hash_maps.unsorted_table_map import UnsortedTableMap


class ChainHashMap(BaseHashMap):
    # O(n)
    def __iter__(self):
        for bucket in self._bucket_array:
            if bucket is not None:
                for key in bucket.keys():
                    yield key

    # O(1) + O(fairly small n)
    def __setitem__(self, key, value):
        i = self._hash_func(key)
        if self._bucket_array[i] is None:
            self._bucket_array[i] = UnsortedTableMap()  # self._bucket_array[i] is called a bucket.

        # __setitem__() can be either an insertion or a replacement.
        old_bucket_size = len(self._bucket_array[i])
        self._bucket_array[i][key] = value
        if len(self._bucket_array[i]) > old_bucket_size:
            self._size += 1

        if self.load_factor() > self._load_factor_threshold:
            self._resize(len(self._bucket_array) * 2 - 1)

    # O(1) + O(fairly small n)
    def __getitem__(self, key):
        i = self._hash_func(key)
        bucket = self._bucket_array[i]
        if bucket is None:
            raise KeyError
        return bucket[key]  # UnsortedTableMap might also raise KeyError.

    # O(1) + O(fairly small n)
    def __delitem__(self, key):
        i = self._hash_func(key)
        bucket = self._bucket_array[i]
        if bucket is None:
            raise KeyError
        del bucket[key]  # UnsortedTableMap might also raise KeyError.

    def distribution_mean(self):
        return statistics.mean([len(bucket) for bucket in self._bucket_array if bucket is not None])

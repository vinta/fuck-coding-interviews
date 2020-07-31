# coding: utf-8
from abc import abstractmethod
from collections.abc import MutableMapping

from algorithms.hashing.mad_compression import mad


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class BaseMap(MutableMapping):
    ITEM_CLASS = Item

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def __len__(self):
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __setitem__(self, key, value):
        ...

    @abstractmethod
    def __getitem__(self, key):
        ...

    @abstractmethod
    def __delitem__(self, key):
        ...


class BaseHashMap(BaseMap):
    def __init__(self, capacity=None, lf_threshold=None):
        # Setting capacity to a prime number can slightly reduce collision.
        self._bucket_array = [None, ] * (capacity if capacity else 11)
        self._size = 0
        self._load_factor_threshold = lf_threshold if lf_threshold else 0.5

    # O(1)
    def __len__(self):
        return self._size

    # O(1)
    def _hash_func(self, key):
        return mad(hash(key), len(self._bucket_array))

    # O(1)
    def _load_factor(self):
        return self._size / len(self._bucket_array)

    # O(n)
    def _resize(self, new_capacity):
        old_items = list(self.items())
        self._bucket_array = [None, ] * new_capacity
        self._size = 0
        for key, value in old_items:
            # __setitem__() will re-hash items and re-calculate _size
            # according to the new capacity of the bucket array.
            self[key] = value

    def _auto_resize(self):
        if self._load_factor() > self._load_factor_threshold:
            self._resize(len(self._bucket_array) * 2 - 1)

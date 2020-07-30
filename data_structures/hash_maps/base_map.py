# coding: utf-8
from abc import abstractmethod
from collections.abc import MutableMapping
import random


class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key

    def __gt__(self, other):
        return self.key > other.key

    def __ge__(self, other):
        return self.key >= other.key


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
    def __init__(self, capacity=None, lf_threshold=None, prime=None):
        # Setting capacity to a prime number can slightly reduce collision.
        self._bucket_array = [None, ] * (capacity if capacity else 11)
        self._size = 0
        self._load_factor_threshold = lf_threshold if lf_threshold else 0.5

        # The following variables are used by MAD compression function.
        self._prime = prime if prime else 109345121
        self._scale = 1 + random.randrange(self._prime - 1)
        self._shift = random.randrange(self._prime)

    # O(1)
    def __len__(self):
        return self._size

    # O(1)
    def _hash_func(self, key):
        """
        It is common to view a hash function, h(k), as consisting of two parts:
        1. A hash code that maps a key k to an integer.
        2. A compression function that maps the hash code to an index within [0, N − 1], for a bucket array.

        We use Python's built-in hash() to produce hash code for key,
        and a randomized Multiply-Add-and-Divide (MAD) formula as compression function:

        ((hash_code * scale + shift) mod P) mod N

        where N is the size of the bucket array,
        P is a prime number larger than N,
        and scale and shift are random integers from the [0, p – 1], with scale > 0.
        """
        return ((hash(key) * self._scale + self._shift) % self._prime) % len(self._bucket_array)

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

    # O(1)
    # O(n) if it triggers resizing
    def _auto_resize(self):
        if self._load_factor() > self._load_factor_threshold:
            self._resize(len(self._bucket_array) * 2 - 1)

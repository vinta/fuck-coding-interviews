# coding: utf-8
"""
LinearProbingHashMap uses Linear Probing (one of Open Addressing methods) as collision resolution strategy.

https://en.wikipedia.org/wiki/Linear_probing
"""
from data_structures.hash_maps.base_map import BaseHashMap


class LinearProbingHashMap(BaseHashMap):
    AVAILABLE_MARKER = object()

    def __iter__(self):
        for item in self._bucket_array:
            if not self._is_empty_or_available(item):
                yield item.key

    def _is_empty_or_available(self, item):
        return (item is None) or (item is self.AVAILABLE_MARKER)

    def __setitem__(self, key, value):
        index = self._hash_func(key)
        while True:
            item = self._bucket_array[index]
            if self._is_empty_or_available(item):
                # Both empty or available bucket can be inserted.
                self._bucket_array[index] = self.ITEM_CLASS(key, value)
                self._size += 1
                self._auto_resize()
                return
            else:
                if item.key == key:
                    item.value = value
                    return
                else:
                    # item.key != key means A[i] is already occupied by another key,
                    # So we try to insert the item at A[(i + 1) mod N], A[(i + 2) mod N], and so on.
                    pass

            index = (index + 1) % len(self._bucket_array)

    def __getitem__(self, key):
        """
        We can only stop searching consecutive slots for key when we encounter an "empty" bucket or the item with that key.
        If we encounter available markers, we simply skip them.
        """
        index = self._hash_func(key)
        while True:
            item = self._bucket_array[index]
            if self._is_empty_or_available(item):
                if item is None:
                    raise KeyError
            else:
                if item.key == key:
                    return item.value

            index = (index + 1) % len(self._bucket_array)

    def __delitem__(self, key):
        index = self._hash_func(key)
        while True:
            item = self._bucket_array[index]
            if self._is_empty_or_available(item):
                if item is None:
                    raise KeyError
            else:
                if item.key == key:
                    self._bucket_array[index] = self.AVAILABLE_MARKER
                    self._size -= 1
                    return

            index = (index + 1) % len(self._bucket_array)

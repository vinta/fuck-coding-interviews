# coding: utf-8
from data_structures.hash_maps.base_map import BaseMap


# This implementation only supports keys of the same type in an instance.
class SortedTableMap(BaseMap):
    def __init__(self):
        self._table = []

    # O(1)
    def __len__(self):
        return len(self._table)

    # O(n)
    def __iter__(self):
        for item in self._table:
            yield item.key

    # O(log n)
    def _insertable_binary_search(self, target_key, low, high):
        # NOTE: If target_key is not in _table,
        # it returns the index that the key should be inserted.
        if low > high:
            # (found, index)
            return (False, high + 1)

        mid = (low + high) // 2
        mid_key = self._table[mid].key
        if target_key == mid_key:
            # There is no duplicate key in a map,
            # so we don't need neither the left or right bound version of Binary Search.
            return (True, mid)
        elif target_key < mid_key:
            return self._insertable_binary_search(target_key, low, mid - 1)
        elif target_key > mid_key:
            return self._insertable_binary_search(target_key, mid + 1, high)

    # O(log n) + O(n)
    def __setitem__(self, key, value):
        found, index = self._insertable_binary_search(key, 0, len(self._table) - 1)
        if found:
            self._table[index].value = value
        else:
            # index might be len(_table) if key is greater than every item in _table.
            self._table.insert(index, self.ITEM_CLASS(key, value))

    # O(log n)
    def __getitem__(self, key):
        found, index = self._insertable_binary_search(key, 0, len(self._table) - 1)
        if found:
            return self._table[index].value
        else:
            raise KeyError

    # O(log n) + O(n)
    def __delitem__(self, key):
        found, index = self._insertable_binary_search(key, 0, len(self._table) - 1)
        if found:
            self._table.pop(index)
        else:
            raise KeyError

    # O(1)
    def find_min(self):
        try:
            item = self._table[0]
        except IndexError:
            return None
        else:
            return (item.key, item.value)

    # O(1)
    def find_max(self):
        try:
            item = self._table[-1]
        except IndexError:
            return None
        else:
            return (item.key, item.value)

    # O(log n) + O(n)
    def find_lt(self, key):
        _, index = self._insertable_binary_search(key, 0, len(self._table) - 1)
        start, stop = 0, index

        for item in self._table[start:stop]:
            yield (item.key, item.value)

    # O(log n) + O(n)
    def find_le(self, key):
        found, index = self._insertable_binary_search(key, 0, len(self._table) - 1)
        if found:
            start, stop = 0, index + 1
        else:
            start, stop = 0, index

        for item in self._table[start:stop]:
            yield (item.key, item.value)

    # O(log n) + O(n)
    def find_gt(self, key):
        found, index = self._insertable_binary_search(key, 0, len(self._table) - 1)
        if found:
            start, stop = index + 1, len(self._table)
        else:
            start, stop = index, len(self._table)

        for item in self._table[start:stop]:
            yield (item.key, item.value)

    # O(log n) + O(n)
    def find_ge(self, key):
        _, index = self._insertable_binary_search(key, 0, len(self._table) - 1)
        start, stop = index, len(self._table)

        for item in self._table[start:stop]:
            yield (item.key, item.value)

    # O(log n) + O(n)
    def find_range(self, start_key, stop_key):
        if start_key > stop_key:
            return

        _, i = self._insertable_binary_search(start_key, 0, len(self._table) - 1)
        while i < len(self._table) and (self._table[i].key < stop_key):
            item = self._table[i]
            yield (item.key, item.value)
            i += 1

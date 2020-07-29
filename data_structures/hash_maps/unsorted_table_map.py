# coding: utf-8
from data_structures.hash_maps.base_map import BaseMap


class UnsortedTableMap(BaseMap):
    def __init__(self):
        self._table = []

    # O(1)
    def __len__(self):
        return len(self._table)

    # O(n)
    def __iter__(self):
        for item in self._table:
            yield item.key

    # O(n)
    def __setitem__(self, key, value):
        for item in self._table:
            if key == item.key:
                item.value = value
                return

        self._table.append(self.ITEM_CLASS(key, value))

    # O(n)
    def __getitem__(self, key):
        for item in self._table:
            if item.key == key:
                return item.value

        raise KeyError

    # O(n)
    def __delitem__(self, key):
        for i, item in enumerate(self._table):
            if item.key == key:
                self._table.pop(i)
                return

        raise KeyError

# coding: utf-8
"""
https://learning.oreilly.com/library/view/Data+Structures+and+Algorithms+in+Python/9781118290279/10_chap05.html#ch005-sec009
"""
import ctypes
import unittest


# A dynamic array is that a list maintains an underlying array that has greater capacity than the current length of the list
# This extra capacity makes it easy to append a new element to the list
class DynamicArray:
    def __init__(self, capacity=2):
        self._size = 0
        self._capacity = capacity
        self._array = self._new_array(self._capacity)

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._array[i]

    def __getitem__(self, index):
        if index >= self._size:
            raise IndexError

        return self._array[index]

    def __setitem__(self, index, value):
        if index >= self._size:
            raise IndexError

        self._array[index] = value

    def _new_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def _expand(self, new_capacity):
        new_array = self._new_array(new_capacity)

        for i, value in enumerate(self._array):
            new_array[i] = value

        self._array = new_array
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._expand(self._capacity * 2)

        # Access the underlying array directly instead of using self.__setitem__
        self._array[self._size] = value
        self._size += 1


class TestCase(unittest.TestCase):
    def setUp(self):
        self.array = DynamicArray()

    def test(self):
        with self.assertRaises(IndexError):
            self.array[0] = 'hello world'

        self.array.append(0)
        self.array.append(1)
        self.array.append(2)
        self.assertEqual(len(self.array), 3)

        self.array[2] = self.array[2] * 10
        self.assertEqual(list(self.array), [0, 1, 20])

        with self.assertRaises(IndexError):
            print(self.array[3])


if __name__ == '__main__':
    unittest.main()

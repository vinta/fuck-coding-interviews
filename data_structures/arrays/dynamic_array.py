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

    # O(1)
    def __len__(self):
        return self._size

    def _positive_index(self, index):
        if index >= 0:
            if index >= self._size:
                raise IndexError
            positive_index = index
        else:
            if abs(index) > self._size:
                raise IndexError
            positive_index = self._size + index  # Convert to the positive index

        return positive_index

    # O(1)
    def __getitem__(self, index):
        positive_index = self._positive_index(index)
        return self._array[positive_index]

    # O(1)
    def __setitem__(self, index, value):
        positive_index = self._positive_index(index)
        self._array[positive_index] = value

    # O(n)
    def __iter__(self):
        for i in range(self._size):
            yield self._array[i]

    def _new_array(self, capacity):
        return (capacity * ctypes.py_object)()

    # O(n)
    def _expand(self, new_capacity):
        new_array = self._new_array(new_capacity)

        for i in range(self._size):
            new_array[i] = self._array[i]

        self._array = new_array
        self._capacity = new_capacity

    # O(1)
    # O(n) if it triggers expand
    def append(self, value):
        if self._size == self._capacity:
            self._expand(self._capacity * 2)

        # Access the underlying array directly instead of using self.__setitem__()
        self._array[self._size] = value
        self._size += 1

    # O(n)
    # O(1) if it pops the last item
    def pop(self, index=-1):
        positive_index = self._positive_index(index)
        pop_value = self._array[positive_index]

        for i in range(positive_index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._array[self._size - 1] = None
        self._size -= 1
        return pop_value

    # O(n)
    def insert_before(self, index, value):
        if self._size == self._capacity:
            self._expand(self._capacity * 2)

        positive_index = self._positive_index(index)
        for i in range(self._size, positive_index, -1):
            self._array[i] = self._array[i - 1]

        self._array[positive_index] = value
        self._size += 1

    # O(n)
    def extend(self, another_array):
        new_size = self._size + len(another_array)
        if new_size > self._capacity:
            self._expand(new_size * 2)

        for i in range(len(another_array)):
            self._array[self._size + i] = another_array[i]

        self._size = new_size


class TestCase(unittest.TestCase):
    def setUp(self):
        self.array = DynamicArray()

    def test__getitem__(self):
        with self.assertRaises(IndexError):
            print(self.array[0])

        with self.assertRaises(IndexError):
            print(self.array[1])

        with self.assertRaises(IndexError):
            print(self.array[-1])

    def test__setitem__(self):
        with self.assertRaises(IndexError):
            self.array[0] = 0

        with self.assertRaises(IndexError):
            self.array[1] = 1

        with self.assertRaises(IndexError):
            self.array[-1] = -1

    def test_append(self):
        self.array.append(0)
        self.array.append(1)
        self.array.append(2)

        self.assertEqual(len(self.array), 3)
        self.assertEqual(list(self.array), [0, 1, 2])

        self.array[0] = self.array[0] * 10
        self.array[1] = self.array[1] * 10
        self.array[2] = self.array[2] * 10
        self.assertEqual(list(self.array), [0, 10, 20])

        with self.assertRaises(IndexError):
            print(self.array[3])

        self.array[-1] = self.array[-1] * -1
        self.array[-2] = self.array[-2] * -1
        self.array[-3] = self.array[-3] * -1
        self.assertEqual(list(self.array), [0, -10, -20])

        with self.assertRaises(IndexError):
            print(self.array[-4])

    def test_pop(self):
        def fill_data(total):
            for i in range(total):
                self.array.append(i)

        fill_data(2)
        self.assertEqual(self.array.pop(0), 0)
        self.assertEqual(self.array.pop(0), 1)
        self.assertEqual(list(self.array), [])

        fill_data(2)
        self.assertEqual(self.array.pop(), 1)
        self.assertEqual(self.array.pop(-1), 0)
        self.assertEqual(list(self.array), [])

        fill_data(5)
        self.assertEqual(self.array.pop(3), 3)
        self.assertEqual(self.array.pop(1), 1)
        self.assertEqual(self.array.pop(-2), 2)
        self.assertEqual(list(self.array), [0, 4])

    def test_insert_before(self):
        with self.assertRaises(IndexError):
            self.array.insert_before(0, 0)

        self.array.append(0)
        self.array.append(1)
        self.array.append(2)
        self.array.insert_before(0, -0.5)
        self.array.insert_before(3, 1.5)
        self.array.insert_before(-3, 0.5)
        self.assertEqual(list(self.array), [-0.5, 0, 0.5, 1, 1.5, 2])

        with self.assertRaises(IndexError):
            self.array.insert_before(6, 6)

    def test_extend(self):
        self.array.extend([0, 1, 2])
        self.assertEqual(list(self.array), [0, 1, 2])

        self.array.extend([3, 4, 5, 6])
        self.assertEqual(list(self.array), [0, 1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()

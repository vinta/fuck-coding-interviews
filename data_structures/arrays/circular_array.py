# coding: utf-8
"""
https://learning.oreilly.com/library/view/data-structures-and/9781118290279/11_chap06.html
"""
import unittest


class CircularArray:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._array = [None, ] * self._capacity
        self._size = 0
        self._front = 0

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
            positive_index = self._size + index

        return positive_index

    # O(1)
    def __getitem__(self, index):
        positive_index = self._positive_index(index)
        actual_index = (self._front + positive_index) % self._capacity
        return self._array[actual_index]

    # O(1)
    def __setitem__(self, index, value):
        positive_index = self._positive_index(index)
        actual_index = (self._front + positive_index) % self._capacity
        self._array[actual_index] = value

    # O(n)
    def __iter__(self):
        for i in range(self._size):
            actual_index = (self._front + i) % self._capacity
            yield self._array[actual_index]

    # O(n)
    def _expand(self, new_capacity):
        new_array = [None, ] * new_capacity
        for i in range(self._size):
            old_index = (self._front + i) % self._capacity
            new_array[i] = self._array[old_index]

        self._array = new_array
        self._capacity = new_capacity
        self._front = 0

    # TODO
    # O(n)
    def _shrink(self, new_capacity):
        pass

    @property
    def _rear(self):
        if self._size == 0:
            raise ValueError
        return (self._front + self._size - 1) % self._capacity

    # O(1)
    # O(n) if it triggers expand
    def append(self, value):
        if self._size == self._capacity:
            self._expand(self._capacity * 2)

        append_index = (self._front + self._size) % self._capacity
        self._array[append_index] = value
        self._size += 1

    # O(n)
    # O(1) if it pops the first or the last item
    def pop(self, index=-1):
        if self._size == 0:
            raise IndexError

        positive_index = self._positive_index(index)
        actual_index = (self._front + positive_index) % self._capacity
        pop_value = self._array[actual_index]

        if actual_index == self._front:  # the first item
            self._array[actual_index] = None
            self._size -= 1
            self._front = (self._front + 1) % self._capacity
        elif actual_index == self._rear:  # the last item
            self._array[actual_index] = None
            self._size -= 1
        else:
            for i in range(positive_index, self._size - 1):
                actual_i = (self._front + i) % self._capacity
                self._array[actual_i] = self._array[actual_i + 1]

            self._array[self._rear] = None
            self._size -= 1

        # TODO
        # if 0 < self._size < (self._capacity * (1 / 4)):
        #     self._shrink(self._capacity // 2)

        return pop_value


class TestCase(unittest.TestCase):
    def setUp(self):
        self.array = CircularArray(4)

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
        self.array.append(3)
        self.array.append(4)
        self.array.append(5)
        self.assertEqual(len(self.array), 6)
        self.assertEqual(list(self.array), [0, 1, 2, 3, 4, 5])

        self.array[0] = self.array[0] * 10
        self.array[1] = self.array[1] * 10
        self.array[2] = self.array[2] * 10
        self.assertEqual(list(self.array), [0, 10, 20, 3, 4, 5])

        with self.assertRaises(IndexError):
            print(self.array[6])

        self.array[-4] = self.array[-4] * -1
        self.array[-5] = self.array[-5] * -1
        self.array[-6] = self.array[-6] * -1
        self.assertEqual(list(self.array), [0, -10, -20, 3, 4, 5])

        with self.assertRaises(IndexError):
            print(self.array[-7])

    def test_pop(self):
        def fill_data(total):
            for i in range(total):
                self.array.append(i)

        fill_data(2)
        self.assertEqual(self.array.pop(), 1)
        self.assertEqual(self.array.pop(), 0)
        self.assertEqual(list(self.array), [])

        fill_data(2)
        self.assertEqual(self.array.pop(0), 0)
        self.assertEqual(self.array.pop(-1), 1)
        self.assertEqual(list(self.array), [])

        fill_data(5)
        self.assertEqual(self.array.pop(3), 3)
        self.assertEqual(self.array.pop(1), 1)
        self.assertEqual(self.array.pop(-2), 2)
        self.assertEqual(list(self.array), [0, 4])

        fill_data(3)
        self.assertEqual(list(self.array), [0, 4, 0, 1, 2])
        self.assertEqual(self.array.pop(0), 0)
        self.assertEqual(self.array.pop(0), 4)
        self.assertEqual(list(self.array), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()

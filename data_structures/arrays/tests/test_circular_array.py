# coding: utf-8
import unittest

from data_structures.arrays.circular_array import CircularArray


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
        self.assertEqual(len(self.array), 6)
        self.assertEqual(list(self.array), [0, 10, 20, 3, 4, 5])

        with self.assertRaises(IndexError):
            print(self.array[6])

        self.array[-4] = self.array[-4] * -1
        self.array[-5] = self.array[-5] * -1
        self.array[-6] = self.array[-6] * -1
        self.assertEqual(len(self.array), 6)
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
        self.assertEqual(len(self.array), 0)
        self.assertEqual(list(self.array), [])

        fill_data(2)
        self.assertEqual(self.array.pop(0), 0)
        self.assertEqual(self.array.pop(-1), 1)
        self.assertEqual(len(self.array), 0)
        self.assertEqual(list(self.array), [])

        fill_data(5)
        self.assertEqual(self.array.pop(3), 3)
        self.assertEqual(self.array.pop(1), 1)
        self.assertEqual(self.array.pop(-2), 2)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(list(self.array), [0, 4])

        fill_data(3)
        self.assertEqual(list(self.array), [0, 4, 0, 1, 2])
        self.assertEqual(self.array.pop(0), 0)
        self.assertEqual(self.array.pop(0), 4)
        self.assertEqual(self.array.pop(1), 1)
        self.assertEqual(self.array.pop(), 2)
        self.assertEqual(len(self.array), 1)
        self.assertEqual(list(self.array), [0, ])

        fill_data(4)
        self.assertEqual(self.array.pop(0), 0)
        self.assertEqual(self.array.pop(), 3)
        self.assertEqual(len(self.array), 3)
        self.assertEqual(list(self.array), [0, 1, 2])


if __name__ == '__main__':
    unittest.main()

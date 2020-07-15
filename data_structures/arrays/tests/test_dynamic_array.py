# coding: utf-8
import unittest

from data_structures.arrays.dynamic_array import DynamicArray


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

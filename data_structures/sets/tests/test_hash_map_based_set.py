# coding: utf-8
import random
import unittest

from data_structures.sets.hash_map_based_set import Set


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_set = Set()

        self.elems = [1, 5, 1, -8, 2, 3, 3, 1, 9]
        self.set = Set(self.elems)
        self.py_set = set(self.elems)

    def test__len__(self):
        self.assertEqual(len(self.empty_set), 0)
        self.assertEqual(len(self.set), len(self.py_set))

    def test__iter__(self):
        self.assertEqual(list(self.empty_set), [])
        self.assertCountEqual(list(self.set), list(self.py_set))

    def test__contains__(self):
        self.assertEqual(1 in self.set, True)
        self.assertEqual(2 in self.set, True)
        self.assertEqual(0 not in self.set, True)
        self.assertEqual(4 not in self.set, True)

    def test_add(self):
        self.set.add(1)
        self.py_set.add(1)
        self.set.add(100)
        self.py_set.add(100)
        self.assertEqual(len(self.set), len(self.py_set))
        self.assertCountEqual(list(self.set), list(self.py_set))

    def test_discard(self):
        self.set.discard(1)
        self.py_set.discard(1)
        self.set.discard(100)
        self.py_set.discard(100)
        self.assertEqual(len(self.set), len(self.py_set))
        self.assertCountEqual(list(self.set), list(self.py_set))

    def test_integration(self):
        for i in range(1, random.randint(2, 10000)):
            self.set.add(i)
            self.py_set.add(i)
            self.assertEqual(i in self.set, True)
            if i % 5 == 0:
                self.set.discard(i)
                self.py_set.discard(i)
                self.assertEqual(i in self.set, False)

        self.assertEqual(len(self.set), len(self.py_set))
        self.assertCountEqual(list(self.set), list(self.py_set))


if __name__ == '__main__':
    unittest.main()

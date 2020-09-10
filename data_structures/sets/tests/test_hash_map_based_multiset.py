# coding: utf-8
from collections import Counter
import unittest

from data_structures.sets.hash_map_based_multiset import Multiset


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_multiset = Multiset()

        self.elements = [1, 5, 1, -8, 2, 3, 3, 1, 9]
        self.multiset = Multiset(self.elements)
        self.counter = Counter(self.elements)

    def test__len__(self):
        self.assertEqual(len(self.empty_multiset), 0)
        self.assertEqual(len(self.multiset), sum(self.counter.values()))

    def test__iter__(self):
        self.assertEqual(list(self.empty_multiset), [])
        self.assertCountEqual(list(self.multiset), self.counter.elements())

    def test__contains__(self):
        self.assertEqual(1 in self.multiset, True)
        self.assertEqual(2 in self.multiset, True)
        self.assertEqual(0 in self.multiset, False)
        self.assertEqual(4 in self.multiset, False)

    def test_add(self):
        self.multiset.add(1)
        self.counter.update({1: 1})
        self.multiset.add(100)
        self.counter.update({100: 1})
        self.assertEqual(len(self.multiset), sum(self.counter.values()))
        self.assertCountEqual(list(self.multiset), self.counter.elements())

    def test_discard(self):
        self.multiset.discard(1)
        self.counter.update({1: -1})
        self.assertEqual(len(self.multiset), sum(self.counter.values()))
        self.assertCountEqual(list(self.multiset), self.counter.elements())

    def test_num_unique_elements(self):
        self.assertEqual(self.multiset.num_unique_elements(), len(self.counter))


if __name__ == '__main__':
    unittest.main()

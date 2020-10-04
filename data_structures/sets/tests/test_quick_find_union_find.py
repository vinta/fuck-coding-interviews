# coding: utf-8
import unittest

from data_structures.sets.quick_find_union_find import QuickFindUnionFind


class TestCase(unittest.TestCase):
    def setUp(self):
        self.union_find = QuickFindUnionFind()
        self.elements = [1, 5, 7, 1, 3, 9, 6, 18, 'A', 'B', 'C']
        for element in self.elements:
            self.union_find.make_set(element)

        self.union_find.union(1, 5)
        self.union_find.union(3, 6)

    def test__len__(self):
        self.assertEqual(len(self.union_find), len(set(self.elements)))

    def test_make_set(self):
        self.union_find.make_set(3.14)
        self.assertEqual(len(self.union_find), len(set(self.elements)) + 1)

    def test_find(self):
        self.assertEqual(self.union_find.find(1), self.union_find.find(5))

    def test_union(self):
        self.union_find.union(1, 7)
        self.assertEqual(self.union_find.find(1), self.union_find.find(7))
        self.assertEqual(self.union_find.find(5), self.union_find.find(7))

        self.union_find.union(1, 3)
        self.assertEqual(self.union_find.find(1), self.union_find.find(3))
        self.assertEqual(self.union_find.find(6), self.union_find.find(3))

    def test_is_connected(self):
        self.assertEqual(self.union_find.is_connected(1, 5), True)
        self.assertEqual(self.union_find.is_connected(1, 9), False)


if __name__ == '__main__':
    unittest.main()

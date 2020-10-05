# coding: utf-8
import unittest

from data_structures.sets.weighted_quick_union_union_find import WeightedQuickUnionUnionFind


class TestCase(unittest.TestCase):
    def setUp(self):
        self.union_find = WeightedQuickUnionUnionFind()
        self.elements = [1, 5, 7, 1, 3, 9, 6, 18, 'A', 'B', 'C']
        self.num_elements = len(set(self.elements))
        for element in self.elements:
            self.union_find.make_group(element)

    def test__init__(self):
        union_pairs = [
            (4, 3),
            (3, 8),
            (6, 5),
            (9, 4),
            (2, 1),
            (8, 9),
            (5, 0),
            (7, 2),
            (6, 1),
            (1, 0),
            (6, 7),
        ]
        union_find = WeightedQuickUnionUnionFind(union_pairs)
        self.assertEqual(union_find.is_connected(4, 3), True)
        self.assertEqual(union_find.is_connected(4, 8), True)
        self.assertEqual(union_find.is_connected(4, 9), True)
        self.assertEqual(union_find.is_connected(4, 6), False)

    def test__len__(self):
        self.assertEqual(len(self.union_find), self.num_elements)

        self.union_find.union(1, 5)
        self.assertEqual(len(self.union_find), self.num_elements - 1)

    def test_make_group(self):
        self.union_find.make_group(3.14)
        self.assertEqual(len(self.union_find), self.num_elements + 1)

    def test_find(self):
        self.union_find.union(1, 5)
        self.assertEqual(self.union_find.find(1), self.union_find.find(5))
        self.assertEqual(len(self.union_find), self.num_elements - 1)

    def test_union(self):
        self.union_find.union(1, 5)
        self.union_find.union(3, 6)
        self.union_find.union(1, 7)
        self.assertEqual(self.union_find.find(1), self.union_find.find(7))
        self.assertEqual(self.union_find.find(5), self.union_find.find(7))
        self.assertEqual(len(self.union_find), self.num_elements - 3)

        self.union_find.union(1, 3)
        self.assertEqual(self.union_find.find(1), self.union_find.find(3))
        self.assertEqual(self.union_find.find(6), self.union_find.find(3))
        self.assertEqual(len(self.union_find), self.num_elements - 4)

        self.union_find.union(1, 42)  # 42 is a new element.
        self.assertEqual(self.union_find.find(5), self.union_find.find(42))

    def test_is_connected(self):
        self.union_find.union(1, 5)
        self.union_find.union(3, 6)
        self.assertEqual(self.union_find.is_connected(1, 5), True)
        self.assertEqual(self.union_find.is_connected(1, 9), False)


if __name__ == '__main__':
    unittest.main()

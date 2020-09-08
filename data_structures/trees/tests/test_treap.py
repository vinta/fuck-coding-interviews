# coding: utf-8
import random
import unittest

from data_structures.trees.treap import Treap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_treap = Treap()
        self.treap = Treap()

        k = random.randint(10, 100)
        self.values = random.sample(range(-1000, 1000), k)
        for value in self.values:
            self.treap.insert(value)

    def test__len__(self):
        self.assertEqual(len(self.empty_treap), 0)
        self.assertEqual(len(self.treap), len(self.values))

    def test__iter__(self):
        self.assertEqual(list(self.empty_treap), [])
        self.assertEqual(list(self.treap), sorted(self.values))

    def test_search(self):
        value = random.choice(self.values)
        node = self.treap.search(value)
        self.assertEqual(node.value, value)

        self.assertEqual(self.empty_treap.search(99999), None)

    def test_insert(self):
        self.empty_treap.insert(99999)
        self.assertEqual(self.empty_treap.root.value, 99999)

    def test_delete(self):
        for value in random.sample(self.values, len(self.values)):
            self.treap.delete(value)

        self.assertEqual(len(self.treap), 0)

        with self.assertRaises(ValueError):
            self.treap.delete(99999)

    def test_check_validation(self):
        priorities = []
        for node in self.treap.levelorder_traverse_nodes():
            node.check_validation()
            priorities.append(node.priority)

        min_priority = min(priorities)
        self.assertEqual(self.treap.root.priority, min_priority)


if __name__ == '__main__':
    unittest.main()

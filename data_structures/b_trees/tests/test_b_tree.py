# coding: utf-8
import random
import unittest

from data_structures.b_trees.b_tree import BTree


class BTreeTest(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(ValueError):
            BTree(order=1)

        self.btree = BTree(order=4)
        self.keys = random.sample(range(1000), k=20)
        self.assertEqual(len(self.keys), len(set(self.keys)))
        for i in self.keys:
            self.btree.insert(key=i, value=f'{i}')

    def test__len__(self):
        self.assertEqual(len(self.btree), 20)

    def test_insert(self):
        btree = BTree(order=3)
        btree.insert(key=42, value='42')
        self.assertEqual(btree.root.keys, [42, ])
        self.assertEqual(btree.root.children, [])

        btree.insert(key=11, value='11')
        self.assertEqual(btree.root.keys, [11, 42])
        self.assertEqual(btree.root.children, [])

        btree.insert(key=27, value='27')
        self.assertEqual(btree.root.keys, [27, ])
        self.assertEqual([node.keys for node in btree.root.children], [[11, ], [42, ]])

        btree.insert(key=4, value='4')
        self.assertEqual(btree.root.keys, [27, ])
        self.assertEqual([node.keys for node in btree.root.children], [[4, 11], [42, ]])

        btree.insert(key=8, value='8')
        self.assertEqual(btree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in btree.root.children], [[4], [11], [42]])

        btree.insert(key=16, value='16')
        self.assertEqual(btree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in btree.root.children], [[4], [11, 16], [42]])

        btree.insert(key=23, value='23')
        self.assertEqual(btree.root.keys, [16, ])
        self.assertEqual([node.keys for node in btree.root.children], [[8], [27]])
        self.assertEqual([node.keys for node in btree.root.children[0].children], [[4], [11]])
        self.assertEqual([node.keys for node in btree.root.children[1].children], [[23], [42]])

        self.assertEqual(list(btree), [4, 8, 11, 16, 23, 27, 42])

    def test_integration(self):
        for _ in range(1000):
            btree = BTree(order=random.randint(2, 128))
            keys = random.sample(range(1000), k=random.randint(1, 1000))
            self.assertEqual(len(keys), len(set(keys)))
            for i in keys:
                btree.insert(key=i, value=f'{i}')


if __name__ == '__main__':
    unittest.main()

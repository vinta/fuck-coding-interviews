# coding: utf-8
import unittest

from data_structures.b_trees.b_tree import BTree


class BTreeTest(unittest.TestCase):
    def setUp(self):
        self.btree = BTree(order=3)

    def test_insert(self):
        self.btree.insert(key=42, value='42')
        self.assertEqual(self.btree.root.keys, [42, ])
        self.assertEqual(self.btree.root.children, [])

        self.btree.insert(key=11, value='11')
        self.assertEqual(self.btree.root.keys, [11, 42])
        self.assertEqual(self.btree.root.children, [])

        self.btree.insert(key=27, value='27')
        self.assertEqual(self.btree.root.keys, [27, ])
        self.assertEqual([node.keys for node in self.btree.root.children], [[11, ], [42, ]])

        self.btree.insert(key=4, value='4')
        self.assertEqual(self.btree.root.keys, [27, ])
        self.assertEqual([node.keys for node in self.btree.root.children], [[4, 11], [42, ]])

        self.btree.insert(key=8, value='8')
        self.assertEqual(self.btree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in self.btree.root.children], [[4], [11], [42]])

        self.btree.insert(key=16, value='16')
        self.assertEqual(self.btree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in self.btree.root.children], [[4], [11, 16], [42]])

        self.btree.insert(key=23, value='23')
        self.assertEqual(self.btree.root.keys, [16, ])
        self.assertEqual([node.keys for node in self.btree.root.children], [[8], [27]])
        self.assertEqual([node.keys for node in self.btree.root.children[0].children], [[4], [11]])
        self.assertEqual([node.keys for node in self.btree.root.children[1].children], [[23], [42]])


if __name__ == '__main__':
    unittest.main()

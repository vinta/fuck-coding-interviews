# coding: utf-8
import random
import unittest

from data_structures.b_trees.b_tree import BTree


class BTreeTest(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(ValueError):
            BTree(order=1)

        self.btree = BTree(order=5)
        self.size = random.randint(1, 1000)
        self.keys = random.sample(range(1000), k=self.size)
        self.assertEqual(len(self.keys), len(set(self.keys)))
        for i in self.keys:
            self.btree.insert(key=i, value=f'{i}')

    def test__len__(self):
        self.assertEqual(len(self.btree), self.size)

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
        self.assertEqual(len(btree), 7)
        self.assertEqual(btree.num_nodes(), 7)

    def test_delete(self):
        btree = BTree(order=4)
        btree.insert(key=42, value='42')
        btree.insert(key=11, value='11')
        btree.insert(key=27, value='27')
        btree.insert(key=4, value='4')
        btree.insert(key=8, value='8')
        btree.insert(key=16, value='16')
        btree.insert(key=23, value='23')

        btree.delete(key=16)
        self.assertEqual(btree.root.keys, [8, 23])
        self.assertEqual([node.keys for node in btree.root.children], [[4], [11], [27, 42]])

        btree.delete(key=4)
        self.assertEqual(btree.root.keys, [23])
        self.assertEqual([node.keys for node in btree.root.children], [[8, 11], [27, 42]])

        btree.delete(key=11)
        self.assertEqual(btree.root.keys, [23])
        self.assertEqual([node.keys for node in btree.root.children], [[8], [27, 42]])

        btree.delete(key=23)
        self.assertEqual(btree.root.keys, [27])
        self.assertEqual([node.keys for node in btree.root.children], [[8], [42]])

        btree.delete(key=8)
        self.assertEqual(btree.root.keys, [27, 42])

        btree.delete(key=42)
        self.assertEqual(btree.root.keys, [27])

        btree.delete(key=27)
        self.assertEqual(btree.root.keys, [])

        self.assertEqual(len(btree), 0)
        self.assertEqual(list(btree), [])

    def test_min_key(self):
        self.assertEqual(self.btree.min_key(), min(self.keys))

    def test_max_key(self):
        self.assertEqual(self.btree.max_key(), max(self.keys))

    def test_check_validation(self):
        btree = BTree(order=random.randint(3, 128))
        keys = random.sample(range(1000), k=random.randint(1, 1000))
        self.assertEqual(len(keys), len(set(keys)))

        inserted_keys = []
        for i in keys:
            btree.insert(key=i, value=f'{i}')
            inserted_keys.append(i)

            if random.randint(1, 10) % 3 == 0:
                random_index = random.randint(0, len(inserted_keys) - 1)
                delete_key = inserted_keys.pop(random_index)
                btree.delete(delete_key)

            for node in btree.levelorder_traverse():
                node.check_validation()

        for i in inserted_keys:
            btree.delete(i)

        self.assertEqual(len(btree), 0)
        self.assertEqual(list(btree), [])


if __name__ == '__main__':
    unittest.main()

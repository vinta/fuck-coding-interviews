# coding: utf-8
import random
import unittest

from data_structures.b_trees.b_tree import BTree


class BTreeTest(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(ValueError):
            BTree(order=2)

        self.b_tree = BTree(order=5)
        self.size = random.randint(1, 1000)
        self.keys = random.sample(range(1000), k=self.size)
        for i in self.keys:
            self.b_tree.insert(key=i, value=f'{i}')

    def test__len__(self):
        self.assertEqual(len(self.b_tree), self.size)

    def test__iter__(self):
        self.assertEqual(list(self.b_tree), sorted(self.keys))

    def test_insert(self):
        b_tree = BTree(order=3)

        b_tree.insert(key=42, value='42')
        self.assertEqual(b_tree.root.keys, [42, ])
        self.assertEqual(b_tree.root.children, [])

        b_tree.insert(key=11, value='11')
        self.assertEqual(b_tree.root.keys, [11, 42])
        self.assertEqual(b_tree.root.children, [])

        b_tree.insert(key=27, value='27')
        self.assertEqual(b_tree.root.keys, [27, ])
        self.assertEqual([node.keys for node in b_tree.root.children], [[11, ], [42, ]])

        b_tree.insert(key=4, value='4')
        self.assertEqual(b_tree.root.keys, [27, ])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4, 11], [42, ]])

        b_tree.insert(key=8, value='8')
        self.assertEqual(b_tree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4], [11], [42]])

        b_tree.insert(key=16, value='16')
        self.assertEqual(b_tree.root.keys, [8, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4], [11, 16], [42]])

        b_tree.insert(key=23, value='23')
        self.assertEqual(b_tree.root.keys, [16, ])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8], [27]])
        self.assertEqual([node.keys for node in b_tree.root.children[0].children], [[4], [11]])
        self.assertEqual([node.keys for node in b_tree.root.children[1].children], [[23], [42]])

        with self.assertRaises(KeyError):
            b_tree.insert(23, '23')

        self.assertEqual(list(b_tree), [4, 8, 11, 16, 23, 27, 42])
        self.assertEqual(len(b_tree), 7)
        self.assertEqual(b_tree.num_nodes(), 7)

    def test_delete(self):
        b_tree = BTree(order=3)
        b_tree.insert(key=42, value='42')
        b_tree.insert(key=11, value='11')
        b_tree.insert(key=27, value='27')
        b_tree.insert(key=4, value='4')
        b_tree.insert(key=8, value='8')
        b_tree.insert(key=16, value='16')
        b_tree.insert(key=23, value='23')

        with self.assertRaises(KeyError):
            b_tree.delete(0)

        b_tree.delete(key=16)
        self.assertEqual(b_tree.root.keys, [11, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[4, 8], [23], [42]])

        b_tree.delete(key=4)
        self.assertEqual(b_tree.root.keys, [11, 27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8], [23], [42]])

        b_tree.delete(key=11)
        self.assertEqual(b_tree.root.keys, [27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8, 23], [42]])

        b_tree.delete(key=23)
        self.assertEqual(b_tree.root.keys, [27])
        self.assertEqual([node.keys for node in b_tree.root.children], [[8], [42]])

        b_tree.delete(key=8)
        self.assertEqual(b_tree.root.keys, [27, 42])

        b_tree.delete(key=42)
        self.assertEqual(b_tree.root.keys, [27])

        b_tree.delete(key=27)
        self.assertEqual(b_tree.root.keys, [])

        self.assertEqual(len(b_tree), 0)
        self.assertEqual(list(b_tree), [])

    def test_min(self):
        self.assertEqual(self.b_tree.min()['key'], min(self.keys))

    def test_max(self):
        self.assertEqual(self.b_tree.max()['key'], max(self.keys))

    def test_check_validation(self):
        order = random.randint(3, 64)
        size = random.randint(1, 5000)

        with self.subTest(order=order, size=size):
            b_tree = BTree(order=order)
            keys = random.sample(range(5000), k=size)
            self.assertEqual(len(keys), len(set(keys)))

            inserted_keys = []
            for i in keys:
                b_tree.insert(key=i, value=f'{i}')
                inserted_keys.append(i)

                if random.randint(1, 10) % 3 == 0:
                    random_index = random.randint(0, len(inserted_keys) - 1)
                    delete_key = inserted_keys.pop(random_index)
                    b_tree.delete(delete_key)

                for node in b_tree.levelorder_traverse_nodes():
                    node.check_validation()

            self.assertEqual(list(b_tree), sorted(inserted_keys))

            for i in inserted_keys:
                b_tree.delete(i)

                for node in b_tree.levelorder_traverse_nodes():
                    node.check_validation()

            self.assertEqual(len(b_tree), 0)
            self.assertEqual(list(b_tree), [])
            self.assertEqual(b_tree.num_nodes(), 1)  # An empty root node.


if __name__ == '__main__':
    unittest.main()

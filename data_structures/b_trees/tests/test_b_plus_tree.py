# coding: utf-8
import random
import unittest

from data_structures.b_trees.b_plus_tree import BPlusTree


class BPlusTreeTest(unittest.TestCase):
    def setUp(self):
        with self.assertRaises(ValueError):
            BPlusTree(order=2)

        self.b_plus_tree = BPlusTree(order=5)
        self.size = random.randint(1, 1000)
        self.keys = random.sample(range(1000), k=self.size)
        for i in self.keys:
            self.b_plus_tree.insert(i, f'{i}')

    def test__len__(self):
        self.assertEqual(len(self.b_plus_tree), self.size)

    def test__iter__(self):
        self.assertEqual(list(self.b_plus_tree), sorted(self.keys))

    def test_get(self):
        for key in self.keys:
            self.assertEqual(self.b_plus_tree.get(key), f'{key}')

        with self.assertRaises(KeyError):
            self.b_plus_tree.get(-1)

    def test_insert(self):
        b_plus_tree = BPlusTree(order=3)

        b_plus_tree.insert(86, '86')
        self.assertEqual(b_plus_tree.root.keys, [86])
        self.assertEqual(b_plus_tree.root.values, ['86'])
        self.assertEqual(list(b_plus_tree), [86])
        self.assertEqual(b_plus_tree.min()['key'], 86)
        self.assertEqual(b_plus_tree.max()['key'], 86)

        with self.assertRaises(KeyError):
            b_plus_tree.insert(86, '86')

        b_plus_tree.insert(99, '99')
        self.assertEqual(b_plus_tree.root.keys, [86, 99])
        self.assertEqual(b_plus_tree.root.values, ['86', '99'])
        self.assertEqual(list(b_plus_tree), [86, 99])
        self.assertEqual(b_plus_tree.min()['key'], 86)
        self.assertEqual(b_plus_tree.max()['key'], 99)

        b_plus_tree.insert(5, '5')
        self.assertEqual(b_plus_tree.root.keys, [86])
        self.assertEqual([leaf.keys for leaf in b_plus_tree.root.values], [[5], [86, 99]])
        self.assertEqual([leaf.values for leaf in b_plus_tree.root.values], [['5'], ['86', '99']])
        self.assertEqual(list(b_plus_tree), [5, 86, 99])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 99)

        b_plus_tree.insert(17, '17')
        self.assertEqual(b_plus_tree.root.keys, [86])
        self.assertEqual([leaf.keys for leaf in b_plus_tree.root.values], [[5, 17], [86, 99]])
        self.assertEqual([leaf.values for leaf in b_plus_tree.root.values], [['5', '17'], ['86', '99']])
        self.assertEqual(list(b_plus_tree), [5, 17, 86, 99])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 99)

        b_plus_tree.insert(24, '24')
        self.assertEqual(b_plus_tree.root.keys, [17, 86])
        self.assertEqual(b_plus_tree.root.values[0].keys, [5])
        self.assertEqual(b_plus_tree.root.values[1].keys, [17, 24])
        self.assertEqual(b_plus_tree.root.values[2].keys, [86, 99])
        self.assertEqual(list(b_plus_tree), [5, 17, 24, 86, 99])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 99)

        b_plus_tree.insert(53, '53')
        self.assertEqual(b_plus_tree.root.keys, [24])
        self.assertEqual(b_plus_tree.root.values[0].keys, [17])
        self.assertEqual(b_plus_tree.root.values[1].keys, [86])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[0].values], [[5], [17]])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[1].values], [[24, 53], [86, 99]])
        self.assertEqual(list(b_plus_tree), [5, 17, 24, 53, 86, 99])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 99)

        b_plus_tree.insert(31, '31')
        self.assertEqual(b_plus_tree.root.keys, [24])
        self.assertEqual(b_plus_tree.root.values[0].keys, [17])
        self.assertEqual(b_plus_tree.root.values[1].keys, [31, 86])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[0].values], [[5], [17]])
        self.assertEqual([leaf_node.keys for leaf_node in b_plus_tree.root.values[1].values], [[24], [31, 53], [86, 99]])
        self.assertEqual(list(b_plus_tree), [5, 17, 24, 31, 53, 86, 99])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 99)

        with self.assertRaises(KeyError):
            b_plus_tree.insert(86, '86')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(99, '99')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(5, '5')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(17, '17')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(24, '24')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(53, '53')

        with self.assertRaises(KeyError):
            b_plus_tree.insert(31, '31')

    def test_delete(self):
        b_plus_tree = BPlusTree(order=3)
        for i in [5, 15, 20, 25, 30, 35, 40, 45]:
            b_plus_tree.insert(i, f'{i}')

        assert b_plus_tree.root.keys == [20, 30]
        assert [child.keys for child in b_plus_tree.root.values] == [[15], [25], [35, 40]]
        assert [child.keys for child in b_plus_tree.root.values[0].values] == [[5], [15]]
        assert [child.keys for child in b_plus_tree.root.values[1].values] == [[20], [25]]
        assert [child.keys for child in b_plus_tree.root.values[2].values] == [[30], [35], [40, 45]]
        self.assertEqual(len(b_plus_tree), 8)
        self.assertEqual(list(b_plus_tree), [5, 15, 20, 25, 30, 35, 40, 45])

        with self.assertRaises(KeyError):
            b_plus_tree.delete(-1)

        b_plus_tree.delete(35)
        assert b_plus_tree.root.keys == [20, 30]
        assert [child.keys for child in b_plus_tree.root.values] == [[15], [25], [40, 45]]
        assert [child.keys for child in b_plus_tree.root.values[0].values] == [[5], [15]]
        assert [child.keys for child in b_plus_tree.root.values[1].values] == [[20], [25]]
        assert [child.keys for child in b_plus_tree.root.values[2].values] == [[30], [40], [45]]
        self.assertEqual(len(b_plus_tree), 7)
        self.assertEqual(list(b_plus_tree), [5, 15, 20, 25, 30, 40, 45])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 45)

        b_plus_tree.delete(40)
        assert b_plus_tree.root.keys == [20, 30]
        assert [child.keys for child in b_plus_tree.root.values] == [[15], [25], [45]]
        assert [child.keys for child in b_plus_tree.root.values[0].values] == [[5], [15]]
        assert [child.keys for child in b_plus_tree.root.values[1].values] == [[20], [25]]
        assert [child.keys for child in b_plus_tree.root.values[2].values] == [[30], [45]]
        self.assertEqual(len(b_plus_tree), 6)
        self.assertEqual(list(b_plus_tree), [5, 15, 20, 25, 30, 45])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 45)

        b_plus_tree.delete(30)
        assert b_plus_tree.root.keys == [20]
        assert [child.keys for child in b_plus_tree.root.values] == [[15], [25, 45]]
        assert [child.keys for child in b_plus_tree.root.values[0].values] == [[5], [15]]
        assert [child.keys for child in b_plus_tree.root.values[1].values] == [[20], [25], [45]]
        self.assertEqual(len(b_plus_tree), 5)
        self.assertEqual(list(b_plus_tree), [5, 15, 20, 25, 45])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 45)

        b_plus_tree.delete(20)
        assert b_plus_tree.root.keys == [25]
        assert [child.keys for child in b_plus_tree.root.values] == [[15], [45]]
        assert [child.keys for child in b_plus_tree.root.values[0].values] == [[5], [15]]
        assert [child.keys for child in b_plus_tree.root.values[1].values] == [[25], [45]]
        self.assertEqual(len(b_plus_tree), 4)
        self.assertEqual(list(b_plus_tree), [5, 15, 25, 45])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 45)

        b_plus_tree.delete(45)
        assert b_plus_tree.root.keys == [15, 25]
        assert [child.keys for child in b_plus_tree.root.values] == [[5], [15], [25]]
        self.assertEqual(len(b_plus_tree), 3)
        self.assertEqual(list(b_plus_tree), [5, 15, 25])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 25)

        b_plus_tree.delete(15)
        assert b_plus_tree.root.keys == [25]
        assert [child.keys for child in b_plus_tree.root.values] == [[5], [25]]
        self.assertEqual(len(b_plus_tree), 2)
        self.assertEqual(list(b_plus_tree), [5, 25])
        self.assertEqual(b_plus_tree.min()['key'], 5)
        self.assertEqual(b_plus_tree.max()['key'], 25)

        b_plus_tree.delete(5)
        assert b_plus_tree.root.keys == [25]
        self.assertEqual(len(b_plus_tree), 1)
        self.assertEqual(list(b_plus_tree), [25])
        self.assertEqual(b_plus_tree.min()['key'], 25)
        self.assertEqual(b_plus_tree.max()['key'], 25)

        b_plus_tree.delete(25)
        assert b_plus_tree.root.keys == []
        self.assertEqual(len(b_plus_tree), 0)
        self.assertEqual(list(b_plus_tree), [])

        with self.assertRaises(KeyError):
            b_plus_tree.min()['key']

        with self.assertRaises(KeyError):
            b_plus_tree.max()['key']

    def test_min(self):
        self.assertEqual(self.b_plus_tree.min()['key'], min(self.keys))

    def test_max(self):
        self.assertEqual(self.b_plus_tree.max()['key'], max(self.keys))

    def test_check_validation(self):
        order = random.randint(3, 64)
        size = random.randint(1, 5000)

        with self.subTest(order=order, size=size):
            b_plus_tree = BPlusTree(order=order)
            keys = random.sample(range(5000), k=size)
            self.assertEqual(len(keys), len(set(keys)))

            inserted_keys = []
            for i in keys:
                b_plus_tree.insert(key=i, value=f'{i}')
                inserted_keys.append(i)

                if random.randint(1, 10) % 3 == 0:
                    random_index = random.randint(0, len(inserted_keys) - 1)
                    delete_key = inserted_keys.pop(random_index)
                    b_plus_tree.delete(delete_key)

                for node in b_plus_tree.levelorder_traverse_nodes():
                    node.check_validation()

            self.assertEqual(list(b_plus_tree), sorted(inserted_keys))

            for i in inserted_keys:
                b_plus_tree.delete(i)

                for node in b_plus_tree.levelorder_traverse_nodes():
                    node.check_validation()

            self.assertEqual(len(b_plus_tree), 0)
            self.assertEqual(list(b_plus_tree), [])


if __name__ == '__main__':
    unittest.main()
